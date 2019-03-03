from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Сообщение',
                                                           'style': 'height:200px'}))

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        # name = self.changed_data.get('name')
        # email = self.changed_data.get('email')
        # message = self.changed_data.get('message')
        #
        # if hasattr(settings, 'ADMIN_EMAIL'):
        #     send_mail(
        #         'Subject here',
        #         'Here is the message.',
        #         'from@example.com',
        #         ['to@example.com'],
        #         fail_silently=False,
        #     )

        print("\nsend_email\n")
        pass
