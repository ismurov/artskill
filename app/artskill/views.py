import csv
from datetime import datetime

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import StreamingHttpResponse

from app.catalogue.models import Product
from .forms import ContactForm, SubscribeForm, UnsubscribeForm
from .models import Subscriber


class IndexView(generic.TemplateView):
    template_name = 'artskill/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'product_hits': Product.objects.order_by('-rating', '-date_updated').all()[:10],
        })
        return context


class BrandView(generic.TemplateView):
    template_name = 'artskill/brand.html'


class ContactsView(generic.TemplateView):
    template_name = 'artskill/contacts.html'


class WhereToBuyView(generic.TemplateView):
    template_name = 'artskill/where_to_buy.html'


class DeliveryView(generic.TemplateView):
    template_name = 'artskill/delivery.html'


class CustomerAgreementView(generic.TemplateView):
    template_name = 'artskill/customer_agreement.html'


class SaleView(generic.ListView):
    template_name = 'artskill/sale.html'
    context_object_name = "products"
    queryset = Product.objects.filter(show_sale_price=True)


class ReturnView(generic.FormView):
    template_name = 'artskill/return.html'
    form_class = ContactForm
    success_url = reverse_lazy('artskill:return-thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email(theme='Возврат')
        return super().form_valid(form)


class ReturnThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Мы свяжемся с вами в ближайшее время.',
    }


class CollaborationView(generic.FormView):
    template_name = 'artskill/collaboration.html'
    form_class = ContactForm
    success_url = reverse_lazy('artskill:collaboration-thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email(theme='Сотрудничество')
        return super().form_valid(form)


class CollaborationThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Мы уже думаем над вашим предложением.',
    }


class RegistrationThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Регистрация прошла успешно.',
    }


class ThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': '',
    }


class SubscribeView(generic.FormView):
    template_name = 'artskill/subscribe.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('artskill:subscribe-thanks')

    def form_valid(self, form):
        subscriber, created = Subscriber.objects.get_or_create(**form.cleaned_data)
        if created:
            form.send_email(theme='Новая подписка на рассылку')
        else:
            if not subscriber.subscribe:
                subscriber.subscribe = True
                subscriber.save()
                form.send_email(theme='Новая подписка на рассылку')

        return super().form_valid(form)


class UnsubscribeView(generic.FormView):
    template_name = 'artskill/unsubscribe.html'
    form_class = UnsubscribeForm
    success_url = reverse_lazy('artskill:unsubscribe-thanks')

    def form_valid(self, form):
        try:
            subscriber = Subscriber.objects.get(email=form.cleaned_data['email'])
        except Subscriber.DoesNotExist:
            subscriber = None

        if subscriber and subscriber.subscribe:
            subscriber.subscribe = False
            subscriber.save()
            form.send_email(theme='Отписка от рассылки')

        return super().form_valid(form)


class SubscribeThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Спасибо, что подписались на наши новости.',
    }


class UnsubscribeThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Мы сожелеем, что вам пришлось отписаться'
                       'от нашей новостной рассылкию.',
    }


class DashboardSubscriberView(PermissionRequiredMixin, generic.ListView):
    queryset = Subscriber.objects.filter(subscribe=True).order_by('email')
    template_name = 'artskill/dashboard/mailing_list.html'
    paginate_by = 100
    permission_required = 'is_staff'
    login_url = reverse_lazy('dashboard:login')


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


class DashboardSubscriberGenCSVFileView(PermissionRequiredMixin, generic.View):
    permission_required = 'is_staff'
    login_url = reverse_lazy('dashboard:login')
    queryset = Subscriber.objects.filter(subscribe=True).order_by('email')

    def get(self, request, *args, **kwargs):
        rows = ([obj.email] for obj in self.queryset.all())
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                         content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="mailing_list_{}.csv"'.format(
            datetime.today().strftime("%d.%m.%Y")
        )
        return response
