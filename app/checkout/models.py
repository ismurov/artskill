from oscar.apps.checkout.models import *  # noqa isort:skip

from decimal import Decimal as D
from decimal import InvalidOperation
from django.conf import settings
from django.dispatch import receiver

from oscar.core.loading import get_model
from app.robokassa.signals import result_received

Order = get_model('order', 'Order')
Source = get_model('payment', 'Source')
SourceType = get_model('payment', 'SourceType')


@receiver(result_received)
def order_paid_handler(sender, **kwargs):
    order_id = kwargs.get('InvId')
    paid_sum = kwargs.get('OutSum', '0')
    try:
        paid_sum = D(paid_sum)
    except InvalidOperation:
        return

    try:
        order = Order.objects.get(number=order_id)
        if order.status == settings.ORDER_PENDING and order.total_incl_tax == paid_sum:
            order.status = settings.ORDER_PAID
            order.save()

        source_type, __ = SourceType.objects.get_or_create(name="Robokassa")
        Source.objects.create(source_type=source_type,
                              amount_allocated=order.total_incl_tax,
                              amount_debited=D(paid_sum),
                              order=order)
    except Order.DoesNotExist:
        pass
