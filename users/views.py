
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def login_user(request):
    if request.method == "POST":
        form=LoginUserForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'], 
            password=cd["password"])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("women:index"))
    else:
        form=LoginUserForm()
    #return HttpResponse('login')
    context={
        "form":form,
    }
    return render(request, "users/login_user.html", context)

def logout_user(request):
    logout(request)
    #return HttpResponse('logout')
    return HttpResponseRedirect(reverse("users:login_user"))

# Create your views here.

