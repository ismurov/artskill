from django import forms
from django.conf import settings

from oscar.core.compat import get_user_model
from oscar.core.loading import get_class, get_model
from oscar.forms.mixins import PhoneNumberMixin

User = get_user_model()
AbstractAddressForm = get_class('address.forms', 'AbstractAddressForm')
Country = get_model('address', 'Country')


class PaymentMethodForm(forms.Form):
    payment_method = forms.ChoiceField(choices=settings.PAYMENT_METHODS, label='Cпособ оплаты')


class ShippingMethodForm(forms.Form):
    method_code = forms.ChoiceField()
    # widget = forms.HiddenInput

    def __init__(self, *args, **kwargs):
        methods = kwargs.pop('methods', [])
        super(ShippingMethodForm, self).__init__(*args, **kwargs)
        self.fields['method_code'].choices = ((m.code, m.name) for m in methods)


class ShippingAddressForm(PhoneNumberMixin, AbstractAddressForm):

    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.adjust_country_field()
        self.fields['line1'].required = False

    def adjust_country_field(self):
        countries = Country._default_manager.filter(
            is_shipping_country=True)

        # No need to show country dropdown if there is only one option
        if len(countries) == 1:
            self.fields.pop('country', None)
            self.instance.country = countries[0]
        else:
            self.fields['country'].queryset = countries
            self.fields['country'].empty_label = None

    class Meta:
        model = get_model('order', 'shippingaddress')
        fields = [
            'title', 'first_name', 'last_name',
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode', 'country',
            'phone_number', 'notes',
        ]
