import random
import itertools

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
def get_color_images(product, num=3):
    if not isinstance(product, Product):
        return []

    exclude = None
    parent = product
    if product.is_child:
        exclude = product
        parent = product.parent

    child_image_sets = [child.get_all_images()[:num]
                        for child in parent.children.all()
                        if child != exclude]
    print(child_image_sets)
    images = list(itertools.chain(*child_image_sets))
    random.shuffle(images)
    return images


@register.simple_tag
def get_sale_percentage(request, product):
    if product.is_parent:
        session = request.strategy.fetch_for_parent(product)
    else:
        session = request.strategy.fetch_for_product(product)

    sale_price = getattr(session.stockrecord, 'cost_price', None)

    if session.price.exists and sale_price:
        if session.price.excl_tax == 0:
            return 100
        elif session.price.is_tax_known:
            return calculate_percentage(session.price.incl_tax, sale_price)
        else:
            return calculate_percentage(session.price.excl_tax, sale_price)


def calculate_percentage(new, full):
    perc = (full - new)/full * 100
    return sale_round(perc)


def sale_round(x, base=5):
    return base * round(x/base)


@register.simple_tag
def delete_wishlist_line_with_ghostly_product(line):
    if isinstance(line, Line) and not line.product:
        line.delete()
