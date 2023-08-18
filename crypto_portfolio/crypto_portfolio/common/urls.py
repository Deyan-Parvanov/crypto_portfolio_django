from django.urls import path

from crypto_portfolio.common.views import index, dashboard, buy_crypto

urlpatterns = (
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('buy/<int:pk>', buy_crypto, name='buy crypto'),
)
