from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name="users"

urlpatterns=[
    #path("login_user/", views.login_user, name="login_user"),
    path("login_user/", views.LoginUser.as_view(), name="login_user"),
    #path("logout_user/", views.logout_user, name="logout_user"),
    path("logout_user/", LogoutView.as_view(), name="logout_user"),
    path("register/", views.register, name="register"),
]

