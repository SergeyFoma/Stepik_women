from django.shortcuts import render
from django.http import HttpResponse
from users.forms import LoginUserForm

def login_user(request):
    form=LoginUserForm()
    #return HttpResponse('login')
    context={
        "form":form,
    }
    return render(request, "users/login_user.html", context)

def logout(request):
    return HttpResponse('logout')

# Create your views here.
