from django import forms

from crypto_portfolio.common.models import UserPortfolio, Order
from crypto_portfolio.core.form_mixins import DisabledFormMixin


class CryptoBuyForm(DisabledFormMixin, forms.ModelForm):
    class Meta:
        model = UserPortfolio
        fields = ('crypto_name', 'crypto_photo', 'crypto_price',
                  'crypto_market_cap', 'crypto_volume', 'quantity',
                  'crypto_user', 'crypto_product',)

        labels = {
            'crypto_name': 'Product',
            'crypto_photo': 'Photo',
            'crypto_price': 'Price',
            'crypto_market_cap': 'Market Cap',
            'crypto_volume': 'Volume',
            'quantity': 'Quantity',
            'crypto_user': 'User',
        }

        widgets = {
            'crypto_name': forms.TextInput(
                attrs={
                    'readonly': True,
                }
            ),
            'crypto_photo': forms.HiddenInput(
                attrs={
                    'readonly': True,
                }
            ),
            'crypto_price': forms.TextInput(
                attrs={
                    'readonly': True,
                }
            ),
            'crypto_market_cap': forms.HiddenInput(
                attrs={
                    'readonly': True,
                }
            ),
            'crypto_volume': forms.HiddenInput(
                attrs={
                    'readonly': True,
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'placeholder': 'Quantity',
                }
            ),
            'crypto_user': forms.HiddenInput(
                attrs={
                    'placeholder': 'User',
                }
            ),
            'crypto_product': forms.HiddenInput(
                attrs={
                    'placeholder': 'Product',
                }
            ),
        }

    disabled_fields = ('crypto_name',)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'customer', 'quantity',)

        labels = {
            'product': 'Product',
            'customer': 'Customer',
            'quantity': 'Quantity',
        }

        widgets = {
            'product': forms.HiddenInput(
                attrs={
                    'readonly': True,
                }
            ),
            'customer': forms.HiddenInput(
                attrs={
                    'readonly': True,
                }
            ),
            'quantity': forms.HiddenInput(
                attrs={
                    'placeholder': 'Quantity',
                    'id': 'order_quantity',
                }
            ),
        }
