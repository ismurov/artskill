from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    # Colors
    NO_COLOR = ''
    BLACK = '#000000'
    GRAY = '#81858b'
    WHITE = '#ffffff'
    RED = '#f53b3b'
    ORANGE = '#ff6500'
    YELLOW = '#f5a623'
    GREEN = '#8ab162'
    LIGHT_BLUE = '#5487ae'
    BLUE = '#3653a5'
    BEIGE = '#f4dfbc'
    OCHER = '#d9b06b'
    BROWN = '#ad7c51'

    COLOR_SET = (
        (NO_COLOR, 'цвет не установлен'),
        (BLACK, 'черные'),
        (GRAY, 'серый'),
        (WHITE, 'белый'),
        (RED, 'красный'),
        (ORANGE, 'оранжевый'),
        (YELLOW, 'желтый'),
        (GREEN, 'зеленый'),
        (LIGHT_BLUE, 'голубой'),
        (BLUE, 'синий'),
        (BEIGE, 'бежевый'),
        (OCHER, 'охра'),
        (BROWN, 'коричневый'),
    )

    description = models.TextField('Краткое описание', blank=True)
    details_description = models.TextField('Подробное описание', blank=True)

    # work with colors
    use_colors = models.BooleanField('Использовать цвета', default=False,
                                     help_text=('Отметьте это пунк, если вы хотите добавлять товары разных цветов.'
                                                ' Товары добавляются в разделе Варианты.'))
    color = models.CharField('Цвет', max_length=24, choices=COLOR_SET, default=NO_COLOR, blank=True)

    # show sale price on/off
    show_sale_price = models.BooleanField('Отображать цену со скидкой',
                                          default=False,
                                          help_text=(
                                              "Этот флаг указывает, будет ли отображаться этот товар в разделе 'SALE'. "
                                              "Отображаемая 'Цена без скидки' указывается в разделе 'Цена и наличие'."))

    rating = models.FloatField('Рейтинг товара', default=0,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(10)],
                               help_text=('Хиты продаж на главной странице выводятся согласно рейтингу.<br>'
                                          'Допустимые значения рейтинга от 0 до 5.'))


from oscar.apps.catalogue.models import *
