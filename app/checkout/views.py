from django.views import generic

from oscar.apps.checkout.views import PaymentDetailsView as OscarPaymentDetailsView


# class IndexView(generic.TemplateView):
#     template_name = 'artskill/checkout_temp.html'


class PaymentDetailsView(OscarPaymentDetailsView):
    pass
