from django.views import generic
from django.shortcuts import render
from django.db import transaction
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from oscar.core.compat import get_user_model
from oscar.core.loading import get_model

# same
# from django.contrib.auth.models import User

from .forms import UserForm, ProfileForm


User = get_user_model()
Order = get_model('order', 'Order')


class ProfileView(generic.View):
    template_name = 'user_profile/user_info.html'
    extra_context = {
        'active_tab': 'profile',
    }

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
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
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            **self.extra_context
        })


class OrdersView(generic.ListView):
    context_object_name = "orders"
    template_name = 'user_profile/orders.html'
    paginate_by = settings.OSCAR_ORDERS_PER_PAGE
    model = Order
    extra_context = {
        'active_tab': 'orders',
    }

    def get_queryset(self):
        return self.model._default_manager.filter(user=self.request.user)


class FavoritesView(generic.View):
    template_name = 'user_profile/favorites.html'
    extra_context = {
        'active_tab': 'wishlists',
    }

    def get(self, request):
        wishlist = self.request.user.wishlists.first()
        return render(request, self.template_name, {
            'wishlist': wishlist,
            **self.extra_context
        })
