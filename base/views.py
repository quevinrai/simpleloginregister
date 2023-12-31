from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ChangeProfileForm, ChangeEmailForm
from .models import CustomUser

User = CustomUser

# Create your views here
def home(request):
    return render(request, 'base/home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist!')

    return render(request, 'base/login.html')

def register_user(request):    
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/register.html', context)

@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        username = request.user.username
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        new_password_confirmation = request.POST.get('new-password-confirmation')

        user = authenticate(request, username=username, password=old_password)

        if user is not None:
            if new_password == new_password_confirmation:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been updated!')

                update_session_auth_hash(request, user)
                return redirect('home')
            else:
                messages.error(request, 'New password doesn\'t match the new password confirmation!')
        else:
            messages.error(request, 'Old password does not match your current password!')

    return render(request, 'base/change_password.html')

@login_required(login_url='login')
def change_profile(request):
    user = User.objects.get(username=request.user.username)
    form = ChangeProfileForm(instance=user)

    if request.method == "POST":
        form = ChangeProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/change_profile.html', context)

@login_required(login_url='login')
def change_email(request):
    user = User.objects.get(username=request.user.username)
    form = ChangeEmailForm(instance=user)

    if request.method == "POST":
        form = ChangeEmailForm(request.POST, instance=user)
        if form.is_valid():
            new_email = form.save(commit=False)
            new_email.email = request.POST.get('new-email')
            new_email.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/change_email.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')