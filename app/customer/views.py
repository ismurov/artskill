from django import http
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.shortcuts import render
from django.db import transaction

from oscar.core.compat import get_user_model
from oscar.core.loading import (
    get_class, get_classes, get_model, get_profile_class)
from oscar.views.generic import PostActionMixin

from .forms import MyUserForm, MyProfileForm


User = get_user_model()
Order = get_model('order', 'Order')

PageTitleMixin, RegisterUserMixin = get_classes(
    'customer.mixins', ['PageTitleMixin', 'RegisterUserMixin'])
Dispatcher = get_class('customer.utils', 'Dispatcher')
EmailAuthenticationForm, EmailUserCreationForm, OrderSearchForm = get_classes(
    'customer.forms', ['EmailAuthenticationForm', 'EmailUserCreationForm',
                       'OrderSearchForm'])
PasswordChangeForm = get_class('customer.forms', 'PasswordChangeForm')
ProfileForm, ConfirmPasswordForm = get_classes(
    'customer.forms', ['ProfileForm', 'ConfirmPasswordForm'])
UserAddressForm = get_class('address.forms', 'UserAddressForm')
Line = get_model('basket', 'Line')
Basket = get_model('basket', 'Basket')


# =============
# Profile
# =============

class ProfileView(generic.View):
    template_name = 'customer/profile/my_profile.html'
    extra_context = {
        'active_tab': 'profile',
    }

    def post(self, request):
        user_form = MyUserForm(request.POST, instance=request.user)
        profile_form = MyProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен.')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            **self.extra_context
        })

    def get(self, request):
        user_form = MyUserForm(instance=request.user)
        profile_form = MyProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            **self.extra_context
        })


# =============
# Order history
# =============

class OrderHistoryView(PageTitleMixin, generic.ListView):
    """
    Customer order history
    """
    context_object_name = "orders"
    template_name = 'customer/order/order_list.html'
    paginate_by = settings.OSCAR_ORDERS_PER_PAGE
    model = Order
    form_class = OrderSearchForm
    page_title = _('Order History')
    active_tab = 'orders'

    def get(self, request, *args, **kwargs):
        if 'date_from' in request.GET:
            self.form = self.form_class(self.request.GET)
            if not self.form.is_valid():
                self.object_list = self.get_queryset()
                ctx = self.get_context_data(object_list=self.object_list)
                return self.render_to_response(ctx)
            data = self.form.cleaned_data

            # If the user has just entered an order number, try and look it up
            # and redirect immediately to the order detail page.
            if data['order_number'] and not (data['date_to'] or
                                             data['date_from']):
                try:
                    order = Order.objects.get(
                        number=data['order_number'], user=self.request.user)
                except Order.DoesNotExist:
                    pass
                else:
                    return redirect(
                        'customer:order', order_number=order.number)
        else:
            self.form = self.form_class()
        return super(OrderHistoryView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        qs = self.model._default_manager.filter(user=self.request.user)
        if self.form.is_bound and self.form.is_valid():
            qs = qs.filter(**self.form.get_filters())
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super(OrderHistoryView, self).get_context_data(*args, **kwargs)
        ctx['form'] = self.form
        return ctx


class OrderDetailView(PageTitleMixin, PostActionMixin, generic.DetailView):
    model = Order
    active_tab = 'orders'

    def get_template_names(self):
        return ["customer/order/order_detail.html"]

    def get_page_title(self):
        """
        Order number as page title
        """
        return u'%s #%s' % (_('Order'), self.object.number)

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user,
                                 number=self.kwargs['order_number'])

    def do_reorder(self, order):  # noqa (too complex (10))
        """
        'Re-order' a previous order.

        This puts the contents of the previous order into your basket
        """
        # Collect lines to be added to the basket and any warnings for lines
        # that are no longer available.
        basket = self.request.basket
        lines_to_add = []
        warnings = []
        for line in order.lines.all():
            is_available, reason = line.is_available_to_reorder(
                basket, self.request.strategy)
            if is_available:
                lines_to_add.append(line)
            else:
                warnings.append(reason)

        # Check whether the number of items in the basket won't exceed the
        # maximum.
        total_quantity = sum([line.quantity for line in lines_to_add])
        is_quantity_allowed, reason = basket.is_quantity_allowed(
            total_quantity)
        if not is_quantity_allowed:
            messages.warning(self.request, reason)
            self.response = redirect('customer:order-list')
            return

        # Add any warnings
        for warning in warnings:
            messages.warning(self.request, warning)

        for line in lines_to_add:
            options = []
            for attribute in line.attributes.all():
                if attribute.option:
                    options.append({
                        'option': attribute.option,
                        'value': attribute.value})
            basket.add_product(line.product, line.quantity, options)

        if len(lines_to_add) > 0:
            self.response = redirect('basket:summary')
            messages.info(
                self.request,
                _("All available lines from order %(number)s "
                  "have been added to your basket") % {'number': order.number})
        else:
            self.response = redirect('customer:order-list')
            messages.warning(
                self.request,
                _("It is not possible to re-order order %(number)s "
                  "as none of its lines are available to purchase") %
                {'number': order.number})


class OrderLineView(PostActionMixin, generic.DetailView):
    """Customer order line"""

    def get_object(self, queryset=None):
        order = get_object_or_404(Order, user=self.request.user,
                                  number=self.kwargs['order_number'])
        return order.lines.get(id=self.kwargs['line_id'])

    def do_reorder(self, line):
        self.response = redirect('customer:order', self.kwargs['order_number'])
        basket = self.request.basket

        line_available_to_reorder, reason = line.is_available_to_reorder(
            basket, self.request.strategy)

        if not line_available_to_reorder:
            messages.warning(self.request, reason)
            return

        # We need to pass response to the get_or_create... method
        # as a new basket might need to be created
        self.response = redirect('basket:summary')

        # Convert line attributes into basket options
        options = []
        for attribute in line.attributes.all():
            if attribute.option:
                options.append({'option': attribute.option,
                                'value': attribute.value})
        basket.add_product(line.product, line.quantity, options)

        if line.quantity > 1:
            msg = _("%(qty)d copies of '%(product)s' have been added to your"
                    " basket") % {
                      'qty': line.quantity, 'product': line.product}
        else:
            msg = _("'%s' has been added to your basket") % line.product

        messages.info(self.request, msg)


class AnonymousOrderDetailView(generic.DetailView):
    model = Order
    template_name = "customer/anon_order.html"

    def get_object(self, queryset=None):
        # Check URL hash matches that for order to prevent spoof attacks
        order = get_object_or_404(self.model, user=None,
                                  number=self.kwargs['order_number'])
        if not order.check_verification_hash(self.kwargs['hash']):
            raise http.Http404()
        return order
