from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        help_text='Optional.'
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        help_text='Optional.'
    )
    email = models.CharField(
        max_length=255,
        unique=True,
        validators=[EmailValidator('Required. Type a valid address.')],
        help_text='Required. Type a valid address.'
    )
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(4)],
        help_text='<ul>' +
            '<li>Your password can\'t be too to your other personal information.</li>' +
            '<li>Your password must contain at least 8 characters.</li>' +
            '<li>Your password can\'t be a commonly used password.</li>' +
            '<li>Your password can\'t be entirely numeric.</li>' +
        '</ul>'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [username, email, password]

    def __str__(self):
        return self.username