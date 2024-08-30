from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from users.models import User

from users.forms import UserLoginForm, UserRegisterForm, UserIdentifierForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'RentVlg - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'RentVlg - Регистрация',
        'form': form
    }

    return render(request, 'users/registration.html', context)

@login_required
def identification(request):

    if request.method == 'POST':
        
        form = UserIdentifierForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserIdentifierForm()

    context = {
        'title': 'RentVlg - Идентификация',
        'form': form
    }

    return render(request, 'users/identification.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))