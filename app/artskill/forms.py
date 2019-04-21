from django import forms
from django.conf import settings
from django.core.mail import mail_admins, send_mail
from django.template.loader import render_to_string


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Сообщение',
                                                           'style': 'height:200px'}))

    def send_email(self, theme='Форма обратной связи'):
        # send email using the self.cleaned_data dictionary
        ctx = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data.get('email'),
            'message': self.cleaned_data.get('message'),
        }
        msg_plain = render_to_string('artskill/emails/collaboration.txt', ctx)

        send_mail(theme,
                  msg_plain,
                  settings.DEFAULT_FROM_EMAIL,
                  [settings.OWNER_EMAIL])


class SubscribeForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def send_email(self, theme='Новая подписка на рассылку'):
        # notify about new subscribe
        ctx = {
            'email': self.cleaned_data.get('email'),
        }
        msg_plain = render_to_string('artskill/emails/new_subscribe_notify.txt', ctx)
        send_mail(theme,
                  msg_plain,
                  settings.DEFAULT_FROM_EMAIL,
                  [settings.OWNER_EMAIL])


class UnsubscribeForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Укажити причину отписки',
                   'style': 'height:200px'})
    )

    def send_email(self, theme='Новая подписка на рассылку'):
        # notify about new subscribe
        ctx = {
            'email': self.cleaned_data.get('email'),
            'message': self.cleaned_data.get('message'),
        }
        msg_plain = render_to_string('artskill/emails/unsubscribe_notify.txt', ctx)
        send_mail(theme,
                  msg_plain,
                  settings.DEFAULT_FROM_EMAIL,
                  [settings.OWNER_EMAIL])
