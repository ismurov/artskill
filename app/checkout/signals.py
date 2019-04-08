from django.conf import settings
from django.dispatch import receiver
from django.core.mail import mail_admins, send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from oscar.apps.checkout.signals import post_checkout


@receiver(post_checkout)
def send_mail_about_order_placed(sender, **kwargs):
    order = kwargs.get('order')
    if order:
        theme = 'Добавлен новый заказ'
        order_url = '{}{}'.format(
            settings.SITE_URL.rstrip('/'),
            reverse('dashboard:order-detail', kwargs={'number': order.number}),
        )
        ctx = {
            'order': order,
            'order_url': order_url,
        }
        msg_plain = render_to_string('oscar/checkout/emails/message_about_new_order_placed.txt', ctx)

        # mail_admins(theme, msg_plain)
        send_mail(theme,
                  msg_plain,
                  settings.DEFAULT_FROM_EMAIL,
                  [settings.OWNER_EMAIL])
