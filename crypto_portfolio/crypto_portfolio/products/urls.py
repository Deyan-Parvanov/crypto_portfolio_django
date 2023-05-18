from django.urls import path, include

from crypto_portfolio.products.views import add_product, details_product, edit_product, delete_product
from crypto_portfolio.common.views import products

urlpatterns = (
    path('add/', add_product, name='add product'),
    path('products/', products, name='products'),
    path('<str:username>/product/<slug:product_slug>/', include([
        path('', details_product, name='details product'),
        path('edit/', edit_product, name='edit product'),
        path('delete/', delete_product, name='delete product'),
    ]))
)
