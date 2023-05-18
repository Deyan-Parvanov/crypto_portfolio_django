from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from crypto_portfolio.products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from crypto_portfolio.products.utils import get_product_by_name_and_username


@login_required
def add_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
    else:
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_user = request.user
            product.save()
            return redirect('products')

    context = {
        'form': form,
    }

    return render(request, 'coins/create-product.html', context)


def details_product(request, username, product_slug):
    product = get_product_by_name_and_username(product_slug, username)
    category = product.category

    context = {
        'category': category,
        'product': product,
        'is_owner': product.product_user == request.user
    }

    return render(request, 'coins/details-product.html', context)


def edit_product(request, username, product_slug):
    product = get_product_by_name_and_username(product_slug, username)

    if request.method == 'GET':
        form = ProductEditForm(instance=product)
    else:
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('details product', username=username, product_slug=product_slug)

    context = {
        'form': form,
        'product_slug': product_slug,
        'username': username,
    }

    return render(request, 'coins/edit-product.html', context)

# class CoinEdit(views.UpdateView):
#     template_name = 'products/edit-product.html'
#     model = Coins
#     fields = ('coin_name', 'coin_photo', 'coin_price', 'coin_market_cap', 'coin_volume', 'coin_user')

    # def get_success_url(self):
    #     return reverse_lazy('details coin', kwargs={
    #         'pk': self.request.user.pk,
    #     })


def delete_product(request, username, product_slug):
    product = get_product_by_name_and_username(product_slug, username)

    if request.method == 'GET':
        form = ProductDeleteForm(instance=product)
    else:
        form = ProductDeleteForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('details user', request.user.pk)

    context = {
        'form': form,
        'product_slug': product_slug,
        'username': username
    }

    return render(request, 'coins/delete-product.html', context)
