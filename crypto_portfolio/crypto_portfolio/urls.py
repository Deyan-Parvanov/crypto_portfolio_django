from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('crypto_portfolio.accounts.urls')),
    path('products/', include('crypto_portfolio.products.urls')),
    path('', include('crypto_portfolio.common.urls')),
]
