from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth.forms import UserChangeForm

from crypto_portfolio.accounts.forms import UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('first_name', 'last_name', 'email',)
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'email',
            'age',
            'profile_picture',
        )}),
        ('Permissions', {
            'fields': ('is_active',
                       'is_staff',
                       'is_superuser',
                       'groups',
                       'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
