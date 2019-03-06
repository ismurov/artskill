from django import template

register = template.Library()


@register.simple_tag
def get_product_parent(product):
    if product and product.is_child:
        return product.parent
    return product