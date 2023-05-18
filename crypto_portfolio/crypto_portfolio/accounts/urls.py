from django.contrib.auth.views import LogoutView
from django.urls import path, include

from crypto_portfolio.accounts.views import SignInView, UserDetailsView, UserEditView, UserDeleteView, SignUpView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='create profile'),
    path('logout/', LogoutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
