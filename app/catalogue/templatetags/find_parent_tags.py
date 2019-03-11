from django import template

from oscar.core.loading import get_model

register = template.Library()

Line = get_model('wishlists', 'Line')
Product = get_model('catalogue', 'Product')


@register.simple_tag
def get_product_parent(product):
    if product and product.is_child:
        return product.parent
    return product


@register.simple_tag
def get_all_images_for_product(product):
    if not isinstance(product, Product):
        return []
    if product.is_child:
        return (*product.get_all_images()[:3], *product.parent.get_all_images()[2:4])
    return product.get_all_images()[2:7]


@register.simple_tag
def delete_wishlist_line_with_ghostly_product(line):
    if isinstance(line, Line) and not line.product:
        line.delete()
