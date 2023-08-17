import collections

from django.shortcuts import render, redirect

from crypto_portfolio.common.forms import CryptoBuyForm, OrderForm
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
    user_products = UserPortfolio.get_products_by_user(request.user.pk)
    product_names = set([product.crypto_name for product in user_products])
    unique_products = {product for product in user_products if product.crypto_name in product_names}



    total_quantity = sum({p.quantity for p in user_products})
    total_price = sum({t.crypto_price for t in user_products})

    context = {
        'user_products': user_products,
        'unique_products': unique_products,
        'total_quantity': total_quantity,
        'total_price': total_price,
    }

    return render(request, 'core/dashboard.html', context)


def buy_crypto(request, pk):
    product = Products.objects.filter(pk=pk).get()
    current_user = request.user.pk

    if request.method == 'GET':
        portfolio_form = CryptoBuyForm(initial={
            'crypto_name': product.name,
            'crypto_photo': product.photo,
            'crypto_price': product.price,
            'crypto_market_cap': product.market_cap,
            'crypto_volume': product.volume,
            'quantity': 0,
            'crypto_user': current_user,
        })
        order_form = OrderForm(initial={
            'product': product.pk,
            'customer': current_user,
            'quantity': 0,
            'crypto_product': product.pk,
        })
    else:
        portfolio_form = CryptoBuyForm(request.POST)
        order_form = OrderForm(request.POST)
        if portfolio_form.is_valid() and order_form.is_valid():

            crypto = portfolio_form.save(commit=False)
            order = order_form.save(commit=False)

            crypto.crypto_user = request.user.pk
            order.customer = request.user

            crypto.save()
            order.save()

            return redirect('dashboard')

    context = {
        'portfolio_form': portfolio_form,
        'order_form': order_form,
        'product': product,
        'current_user': current_user,
    }

    return render(request, 'core/buy-product.html', context)
