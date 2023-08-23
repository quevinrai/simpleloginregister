from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.forms import MultiWidget, PasswordInput, TextInput
from django.forms.fields import EmailField
from django.forms.forms import Form
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        required=True, min_length=5,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        label='First Name',
        help_text='Optional.',
        min_length=5,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label='Last Name',
        help_text='Optional.',
        min_length=5,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        label='Email',
        help_text='Required. Type a valid email address.',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '@'})
    )
    password1 = forms.CharField(
        label='Password',
        help_text=mark_safe(
            '<ul> \
                <li>Your password can\'t be too similar to your other personal information.</li> \
                <li>Your password must contain at least 8 characters.</li> \
                <li>Your password can\'t be a commonly used password.</li> \
                <li>Your password cannot be entirely numeric.</li> \
            </ul>'
        ),
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        help_text='Required. Enter the same password as before, for verification.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'})
    )

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError('User already exists!')
        return username
    
    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError('Email already exists!')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match!')
        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )

        return user