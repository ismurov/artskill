from oscar.apps.dashboard.catalogue import forms as base_forms


class ProductForm(base_forms.ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].required = False

    class Meta(base_forms.ProductForm.Meta):
        fields = (
            'title', 'upc', 'description', 'details_description',
            'is_discountable', 'structure', 'use_colors', 'color')
