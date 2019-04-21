from django import template
from app.artskill.forms import SubscribeForm

register = template.Library()


@register.simple_tag
def subscribe_form():
    return SubscribeForm()
