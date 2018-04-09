from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from .forms import UserRegistrationForm
from .forms import UserForm


def home(request):
    return render(request, 'mysite/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                raise forms.ValidationError('A username or email already exists !!!')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_active and not request.user.is_superuser:

        if request.method == 'POST':
            form = UserForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                return HttpResponse('Data Updated Successfully')
        else:
            form = UserForm(instance=request.user)

        context = {
            'form': form,
        }

        return render(request, 'mysite/profile.html', context)
    else:
        return redirect('/admin/')


