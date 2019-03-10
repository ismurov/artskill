from oscar.apps.customer.models import *  # noqa isort:skip

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from oscar.core.compat import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    M = 'M'
    F = 'F'
    GENDER_CHOICES = (
        (M, 'Мужской'),
        (F, 'Женский'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

