from oscar.apps.customer.forms import *

from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .models import Profile


class MyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'email': 'Электронная почта',
        }


class MyProfileForm(forms.ModelForm):
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
        if data and data > timezone.localdate(timezone.now()):
            raise forms.ValidationError("Укажите корректную дату рождения")
        return data


class EmailAuthenticationForm(AuthenticationForm):
    """
    Extends the standard django AuthenticationForm, to support 75 character
    usernames. 75 character usernames are needed to support the EmailOrUsername
    auth backend.
    """
    username = forms.EmailField(
        label=_('Email address'),
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'placeholder': 'Email'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••••••••'}),
    )
    redirect_url = forms.CharField(
        widget=forms.HiddenInput, required=False)

    def __init__(self, host, *args, **kwargs):
        self.host = host
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean_redirect_url(self):
        url = self.cleaned_data['redirect_url'].strip()
        if url and is_safe_url(url, self.host):
            return url


class EmailUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Ваше имя',
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(
        label=_('Email address'),
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••••••••'}))
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••••••••'}))
    redirect_url = forms.CharField(
        required=False,
        widget=forms.HiddenInput)
    subscribe = forms.BooleanField(
        label='Подписаться на рассылку',
        required=False)

    class Meta:
        model = User
        fields = ('first_name', 'email',)

    def __init__(self, host=None, *args, **kwargs):
        self.host = host
        super(EmailUserCreationForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        """
        Checks for existing users with the supplied email address.
        """
        email = normalise_email(self.cleaned_data['email'])
        if User._default_manager.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                _("A user with that email address already exists"))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', '')
        password2 = self.cleaned_data.get('password2', '')
        if password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match."))
        validate_password(password2, self.instance)
        return password2

    def clean_redirect_url(self):
        url = self.cleaned_data['redirect_url'].strip()
        if url and is_safe_url(url, self.host):
            return url
        return settings.LOGIN_REDIRECT_URL

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if 'username' in [f.name for f in User._meta.fields]:
            user.username = generate_username()
        if commit:
            user.save()
        return user
