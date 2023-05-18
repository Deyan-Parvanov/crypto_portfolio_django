from django.shortcuts import render, redirect

from crypto_portfolio.accounts.forms import UserModel
from crypto_portfolio.common.forms import CryptoBuyForm
from crypto_portfolio.common.models import UserPortfolio
from crypto_portfolio.products.model_products import Products


def index(request):

    return render(request, 'core/home-page.html')


def products(request):
    all_products = Products.get_products()

    context = {
        'products': all_products,
    }

    return render(request, 'coins/products.html', context)


def dashboard(request):
    user_products = Products.get_products()

    context = {
        'user_products': user_products,
    }

    return render(request, 'core/dashboard.html', context)


def buy_crypto(request, pk):
    product = Products.objects.filter(pk=pk).get()

    # user = UserModel
    # form = CryptoBuyForm(instance=product)

    if request.method == 'GET':
        form = CryptoBuyForm(instance=product)
    else:
        form = CryptoBuyForm(request.POST, instance=product)
        if form.is_valid():
            # UserPortfolio.objects.all().delete()
            crypto = form.save(commit=False)
            crypto.crypto_user = request.user
            crypto.save()

            # name = request.POST.get('name')
            # photo = request.POST.get('photo')
            # price = request.POST.get('price')
            # market_cap = request.POST.get('market_cap')
            # volume = request.POST.get('volume')
            #
            # UserPortfolio.objects.create(primary_key=True)
            # UserPortfolio.objects.create(crypto_name=name)
            # UserPortfolio.objects.create(crypto_photo=photo)
            # UserPortfolio.objects.create(crypto_price=price)
            # UserPortfolio.objects.create(crypto_market_cap=market_cap)
            # UserPortfolio.objects.create(crypto_volume=volume)
            # UserPortfolio.objects.create(crypto_user=user.pk)
            # UserPortfolio.objects.create(crypto_product=product.pk)

            return redirect('dashboard')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'core/buy-product.html', context)
