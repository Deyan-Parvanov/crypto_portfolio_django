from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password1', 'password2', 'age')
        fields_classes = {'username': auth_forms.UsernameField}


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        field_classes = {"username": auth_forms.UsernameField}
