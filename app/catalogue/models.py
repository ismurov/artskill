from django.db import models
from django.utils.translation import ugettext_lazy as _

from oscar.apps.catalogue.abstract_models import \
    AbstractProduct, AbstractProductAttribute, \
    AbstractProductAttributeValue


class Product(AbstractProduct):
    details_description = models.TextField('Подробное описание', blank=True)


# class ProductAttribute(AbstractProductAttribute):
#     # Attribute types
#     TEXT = "text"
#     INTEGER = "integer"
#     BOOLEAN = "boolean"
#     FLOAT = "float"
#     RICHTEXT = "richtext"
#     DATE = "date"
#     DATETIME = "datetime"
#     OPTION = "option"
#     MULTI_OPTION = "multi_option"
#     ENTITY = "entity"
#     FILE = "file"
#     IMAGE = "image"
#
#     COLOR_SET = "colors"
#
#     TYPE_CHOICES = (
#         (TEXT, _("Text sdfdsfs")),
#         (INTEGER, _("Integer")),
#         (BOOLEAN, _("True / False")),
#         (FLOAT, _("Float")),
#         (RICHTEXT, _("Rich Text")),
#         (DATE, _("Date")),
#         (DATETIME, _("Datetime")),
#         (OPTION, _("Option")),
#         (MULTI_OPTION, _("Multi Option")),
#         (ENTITY, _("Entity")),
#         (FILE, _("File")),
#         (IMAGE, _("Image")),
#
#         (COLOR_SET, _("Colors")),
#     )
#
#     @property
#     def is_multi_option(self):
#         return self.type in [self.MULTI_OPTION, self.COLOR_SET]
#
#     def _validate_colors(self, value):
#         return self._validate_multi_option(value)
#
# class ProductAttributeValue(AbstractProductAttributeValue):
#     pass


from oscar.apps.catalogue.models import *