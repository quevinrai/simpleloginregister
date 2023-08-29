from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ChangeProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']

class ChangeEmailForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']