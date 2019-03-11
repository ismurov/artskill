from django import template

from oscar.core.loading import get_model

register = template.Library()

Line = get_model('wishlists', 'Line')


@register.simple_tag
def get_product_parent(product):
    if product and product.is_child:
        return product.parent
    return product


@register.simple_tag
def delete_wishlist_line_with_ghostly_product(line):
    if isinstance(line, Line) and not line.product:
        line.delete()
