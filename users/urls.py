#<<<<<<< HEAD
from django.urls import path
from . import views

app_name="users"

urlpatterns=[
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
#=======
from django.urls import path
from . import views

app_name="users"

urlpatterns=[
    path("login_user/", views.login_user, name="login_user"),
    path("logout/", views.logout, name="logout"),
]
#>>>>>>> 1950fdc6c22b0fb305be059d47f9c2a0f234da8d
