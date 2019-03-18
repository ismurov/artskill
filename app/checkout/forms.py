from django import forms
from django.conf import settings


class PaymentMethodForm(forms.Form):
    payment_method = forms.ChoiceField(choices=settings.PAYMENT_METHODS, label='Cпособ оплаты')
