from django import forms
from django.core.mail import mail_admins
from django.template.loader import render_to_string

from .models import Subscriber


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
        msg_html = render_to_string('artskill/emails/collaboration.html', ctx)

        mail_admins(theme,
                    msg_plain,
                    # fail_silently=False,
                    html_message=msg_html)


class SubscriberForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))



