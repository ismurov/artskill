from oscar.apps.basket.forms import *  # noqa isort:skip

from django import forms
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_model
from oscar.forms import widgets


class BasketVoucherForm(forms.Form):
    code = forms.CharField(max_length=128, label=_('Code'),
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Введите промокод',}))

    def __init__(self, *args, **kwargs):
        super(BasketVoucherForm, self).__init__(*args, **kwargs)

    def clean_code(self):
        return self.cleaned_data['code'].strip().upper()

