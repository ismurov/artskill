from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    # Colors
    NO_COLOR = ''
    BLACK = '#000000'
    GRAY = '#81858b'
    BROWN = '#ad7c51'
    WHITE = '#ffffff'
    BEIGE = '#f4dfbc'
    GREEN = '#8ab162'
    RED = '#f53b3b'
    YELLOW = '#f5a623'
    BLUE = '#3653a5'
    OCHER = '#d9b06b'
    LIGHT_BLUE = '#5487ae'

    COLOR_SET = (
        (NO_COLOR, 'цвет не установлен'),
        (BLACK, 'черные'),
        (GRAY, 'серый'),
        (BROWN, 'коричневый'),
        (WHITE, 'белый'),
        (BEIGE, 'бежевый'),
        (GREEN, 'зеленый'),
        (RED, 'красный'),
        (YELLOW, 'желтый'),
        (BLUE, 'синий'),
        (OCHER, 'охра'),
        (LIGHT_BLUE, 'голубой'),
    )

    description = models.TextField('Краткое описание', blank=True)
    details_description = models.TextField('Подробное описание', blank=True)

    # work with colors
    use_colors = models.BooleanField('Использовать цвета', default=False,
                                     help_text=('Отметьте это пунк, если вы хотите добавлять товары разных цветов.'
                                                ' Товары добавляются в разделе Варианты.'))
    # color = models.IntegerField('Цвет', choices=COLOR_SET, default=NO_COLOR)
    color = models.CharField('Цвет', max_length=24, choices=COLOR_SET, default=NO_COLOR, blank=True)


from oscar.apps.catalogue.models import *
