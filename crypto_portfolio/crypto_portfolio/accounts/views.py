from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_view, get_user_model

from crypto_portfolio.accounts.forms import UserCreateForm
from crypto_portfolio.common.models import UserPortfolio

UserModel = get_user_model()


class SignInView(auth_view.LoginView):
    # profile = AppUser.objects.first()
    template_name = 'profile/login-profile.html'


class SignUpView(views.CreateView):
    template_name = 'profile/create-profile.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'profile/details-profile.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_products = UserPortfolio.objects.count()
        total_value = sum([crypto.crypto_price for crypto in UserPortfolio.objects.all()])
        context['user'] = self.request.user == self.object
        context['products_count'] = user_products
        context['total_portfolio_value'] = total_value

        return context


class UserEditView(views.UpdateView):
    template_name = 'profile/edit-profile.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'age', 'email', 'profile_picture')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'profile/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('index')
