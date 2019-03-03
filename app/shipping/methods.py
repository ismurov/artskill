from decimal import Decimal as D

from oscar.apps.shipping import methods
from oscar.core import prices


class TakeAway(methods.Free):
    code = 'take_away'
    name = 'Самовывоз'
    description = ('<p>Товар можете забрать в нашем офисе по адресу:</p>'
                   '<p>улица Цветочная, 6M</p>'
                   '<p>Стоимость: бесплатно</p>'
                   '<p>Оплата: сейчас или при получении</p>')


class Standard(methods.Base):
    code = 'standard'
    name = 'Курьерская по Санкт-Петербургу'
    description = ('<p>Стоимость: 300 Р</p>'
                   '<p>Срок доставки: 1-2 д</p>'
                   '<p>Оплата: сейчас или при получении</p>')

    _free_price_from = D('5000.00')
    _standard_price = {'excl_tax': D('300.00'),
                       'incl_tax': D('300.00')}

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


class TakeAwayBoxberry(methods.FixedPrice):
    code = 'boxberry-take-away'
    name = 'Пункт выдачи Boxberry'
    charge_excl_tax = D('1000.00')


class Boxberry(methods.FixedPrice):
    code = 'boxberry-currier'
    name = 'Курьерская доставка Boxberry'
    charge_excl_tax = D('1000.00')
