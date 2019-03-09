from django.db import models
from django.conf import settings


class Subscriber(models.Model):
    email = models.EmailField(help_text='Email адрес подписчика', unique=True)
    subscribe = models.BooleanField(help_text='Состояние подписки', default=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return 'Subscriber #{}: {} (status: {})'.format(
            self.id, self.email, self.subscribe)


class SliderItem(models.Model):
    extra_title = models.CharField('Пометка', max_length=255, blank=True)
    title = models.CharField('Заголовок', max_length=255, blank=True)
    description = models.TextField('Описание', blank=True)

    link = models.CharField(max_length=255, default='#')
    link_title = models.CharField(max_length=255, blank=True)

    image = models.ImageField(
        upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255,
        blank=True, null=True)

    class Meta:
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Элементы слайдера'

    def __str__(self):
        return 'SliderIrem #{}: {}'.format(self.id, self.title)


# class Bestsellers(models.Model):
#     product = models.ForeignKey()
#
#     class Meta:
#         verbose_name = 'Хит продаж'
#         verbose_name_plural = 'Хиты продаж'
#
#     def __str__(self):
#         return 'Bestseller #{}: {}'.format(self.id, self.title)
