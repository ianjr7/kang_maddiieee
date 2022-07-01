from contextlib import redirect_stdout
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_home(request):

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

        #signing up

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    
    context = {'form': form}
    return render(request, 'base/login.html', context)



def logout_user(request):
    logout(request)
    return redirect('login_home')


def home(request):
    return render(request, 'base/home.html') 


def later(request):
    return render(request, 'base/delete_later.html')


def index(request):
    return render(request, 'base/index.html')
   


def meetings(request):
    return render(request, 'base/meetings.html')

def about(request):
    return render(request, 'base/about.html')
   


