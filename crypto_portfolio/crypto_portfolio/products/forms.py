from django import forms

from crypto_portfolio.products.model_products import Products
from crypto_portfolio.core.form_mixins import DisabledFormMixin


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'category', 'photo', 'price', 'market_cap', 'volume')

        labels = {
            'name': 'Name',
            'category': 'Category',
            'photo': 'Image URL',
            'price': 'Price',
            'market_cap': 'Market Cap',
            'volume': 'Volume',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                }
            ),
            'category': forms.TextInput(
                attrs={
                    'placeholder': 'Category',
                }
            ),
            'photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
            'market_cap': forms.TextInput(
                attrs={
                    'placeholder': 'Market Cap',
                }
            ),
            'volume': forms.TextInput(
                attrs={
                    'placeholder': 'Volume',
                }
            ),
        }


class ProductCreateForm(ProductBaseForm):
    pass


class ProductEditForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('name',)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class ProductDeleteForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('name', 'price', 'market_cap', 'volume')

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
