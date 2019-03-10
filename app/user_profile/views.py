from django.views import generic
from django.shortcuts import render
from django.db import transaction
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from oscar.core.compat import get_user_model

# same
# from django.contrib.auth.models import User

from .forms import UserForm, ProfileForm

User = get_user_model()


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


class OrdersView(generic.TemplateView):
    template_name = 'user_profile/orders.html'
    extra_context = {
        'active_tab': 'orders',
    }


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
