from django import forms
from django.utils import timezone

from .models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'email': 'Электронная почта',
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'birth_date', 'gender')
        YEARS = [x for x in range(2020, 1940, -1)]
        widgets = {
            'birth_date': forms.SelectDateWidget(years=YEARS),
            'gender': forms.RadioSelect(),
        }
        labels = {
            'phone': 'Телефон',
            'birth_date': 'Дата рождения',
            'gender': 'Пол',
        }

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        if data > timezone.localdate(timezone.now()):
            raise forms.ValidationError("Укажите корректную дату рождения")
        return data
