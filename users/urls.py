from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from . import views

app_name="users"

urlpatterns=[
    #path("login_user/", views.login_user, name="login_user"),
    path("login_user/", views.LoginUser.as_view(), name="login_user"),
    #path("logout_user/", views.logout_user, name="logout_user"),
    path("logout_user/", LogoutView.as_view(), name="logout_user"),
    #path("register/", views.register, name="register"),
    path("register/", views.RegisterUser.as_view(),name="register"),
    #path("profile/", views.profile, name="profile"),
    #path("profile/<int:pk>/", views.ProfileUser.as_view(),name="profile"),
    path("profile/", views.ProfileUser.as_view(),name="profile"),
    #path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change/", views.UserPasswordChange.as_view(), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(
        template_name="users/password_change_done.html"), name="password_change_done"),

]

