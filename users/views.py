#<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

# Create your views here.
#=======
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
#>>>>>>> 1950fdc6c22b0fb305be059d47f9c2a0f234da8d
