from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here
def home(request):
    return redirect('login')

def login(request):
    if request.method == "POST":
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        print(request.POST.get('remember_me'))

    return render(request, 'base/login.html')

def register(request):
    form = UserCreationForm()

    context = {'form': form}
    return render(request, 'base/register.html', context)