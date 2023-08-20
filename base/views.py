from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here
def home(request):
    return render(request, 'base/home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(request.POST.get('remember_me'))

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist!')

    return render(request, 'base/login.html')

def register_user(request):
    form = UserCreationForm()

    context = {'form': form}
    return render(request, 'base/register.html', context)

def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        new_password_confirmation = request.POST.get('new-password-confirmation')

        

    return render(request, 'base/change_password.html')

def logout_user(request):
    logout(request)
    return redirect('home')