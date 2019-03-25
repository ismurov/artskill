from django import template
from oscar.core.loading import get_model

register = template.Library()
RawHTML = get_model('promotions', 'RawHTML')


@register.simple_tag
def get_promo_page(pages, name):
    if not isinstance(pages, (list, tuple)):
        return
    for page in pages:
        if isinstance(page, RawHTML) and page.name == name:
            return page
