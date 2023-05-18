from django import forms

from crypto_portfolio.common.models import UserPortfolio


class CryptoBuyForm(forms.ModelForm):

    # def save(self, commit=True):
    #     product = super(CryptoBuyForm, self).save(commit=False)
    #
    #     self.fields['crypto_name'] = product.name
    #
    #     if commit:
    #         product.save()
    #     return product

    class Meta:
        model = UserPortfolio
        fields = ('crypto_name', 'crypto_photo', 'crypto_price', 'crypto_market_cap', 'crypto_volume')

        labels = {
            'name': 'Name',
            'photo': 'Image URL',
            'price': 'Price',
            'market_cap': 'Market Cap',
            'volume': 'Volume',
        }
