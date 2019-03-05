from django import template
from app.artskill.forms import SubscriberForm

register = template.Library()


@register.simple_tag
def subscribe_form():
    return SubscriberForm()
