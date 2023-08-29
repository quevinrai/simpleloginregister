from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('change-password', views.change_password, name='change-password'),
    path('change-profile', views.change_profile, name='change-profile'),
    path('change-email', views.change_email, name='change-email'),
    path('logout', views.logout_user, name='logout'),
]
