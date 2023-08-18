from django.contrib.auth import forms as auth_forms, get_user_model, authenticate, login, logout

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password1', 'password2', 'age')
        fields_classes = {'username': auth_forms.UsernameField}

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        user = authenticate(username=username, password1=password1, password2=password2)
        if user:
            raise auth_forms.ValidationError("This username already exists!")
        if password1 != password2:
            raise auth_forms.ValidationError("Passwords does not match!")

        return super(UserCreateForm, self).clean()



class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        field_classes = {"username": auth_forms.UsernameField}
