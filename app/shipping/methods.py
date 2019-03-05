from decimal import Decimal as D

from django.conf import settings

from oscar.apps.shipping import methods
from oscar.core import prices


shipping = settings.SHIPPING_METHODS_STANDARD_OPTIONS

class Standard(methods.Base):
    code = 'standard'
    name = shipping[code]['name']
    description = shipping[code]['description']

    _free_price_from = D(shipping[code]['free_price_from'])
    _standard_price = {'excl_tax': D(shipping[code]['excl_tax']),
                       'incl_tax': D(shipping[code]['incl_tax'])}

    def _free_shipping_conditions(self, basket):
        # price with tax and discount
        if basket.total_incl_tax >= self._free_price_from:
            return True

    def calculate(self, basket):
        if self._free_shipping_conditions(basket):
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'), incl_tax=D('0.00'))
        else:
            return prices.Price(
                currency=basket.currency,
                excl_tax=self._standard_price['excl_tax'],
                incl_tax=self._standard_price['incl_tax'])


class StandardTakeAway(methods.Free):
    code = 'standard-take-away'
    name = shipping[code]['name']
    description = shipping[code]['description']


class Boxberry(methods.FixedPrice):
    code = 'boxberry-currier'
    name = shipping[code]['name']
    description = shipping[code]['description']
    charge_excl_tax = D(shipping[code]['base_price'])


class TakeAwayBoxberry(methods.FixedPrice):
    code = 'boxberry-take-away'
    name = shipping[code]['name']
    description = shipping[code]['description']
    charge_excl_tax = D(shipping[code]['base_price'])
