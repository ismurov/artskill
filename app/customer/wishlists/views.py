# -*- coding: utf-8 -*-

from django.views import generic
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from oscar.core.utils import safe_referrer
from oscar.apps.customer.wishlists import views


class WishListRemoveProduct(views.WishListRemoveProduct):
    def get_success_url(self):
        # msg = _("'%(title)s' was removed from your '%(name)s' wish list") % {
        #     'title': self.line.get_title(),
        #     'name': self.wishlist.name}

        msg = "{title} удален из списка желаемого.".format(
            title=self.line.get_title())
        messages.success(self.request, msg)

        # We post directly to this view on product pages; and should send the
        # user back there if that was the case
        return safe_referrer(self.request, '')


class WishListListView(generic.View):
    template_name = 'customer/wishlists/my_wishlists_list.html'
    extra_context = {
        'page_title': 'Избранное',
        'active_tab': 'wishlists',
    }

    def get(self, request):
        wishlist = self.request.user.wishlists.first()
        return render(request, self.template_name, {
            'wishlist': wishlist,
            **self.extra_context
        })
