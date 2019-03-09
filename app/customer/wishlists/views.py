# -*- coding: utf-8 -*-
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from oscar.core.utils import safe_referrer
from oscar.apps.customer.wishlists import views


class WishListRemoveProduct(views.WishListRemoveProduct):
    def get_success_url(self):
        msg = _("'%(title)s' was removed from your '%(name)s' wish list") % {
            'title': self.line.get_title(),
            'name': self.wishlist.name}
        messages.success(self.request, msg)

        # We post directly to this view on product pages; and should send the
        # user back there if that was the case
        return safe_referrer(self.request, '')