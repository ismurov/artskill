from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(help_text='Email адрес подписчика', unique=True)
    subscribe = models.BooleanField(help_text='Состояние подписки', default=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return 'Subscriber #{}: {} (status: {})'.format(
            self.id, self.email, self.subscribe)
