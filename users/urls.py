
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
)


app_name = "users"

urlpatterns = [
    # path("login_user/", views.login_user, name="login_user"),
    path("login_user/", views.LoginUser.as_view(), name="login_user"),
    # path("logout_user/", views.logout_user, name="logout_user"),
    path("logout_user/", LogoutView.as_view(), name="logout_user"),
    # path("register/", views.register, name="register"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    # path("profile/", views.profile, name="profile"),
    # path("profile/<int:pk>/", views.ProfileUser.as_view(),name="profile"),
    path("profile/", views.ProfileUser.as_view(), name="profile"),
    # path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password-change/", views.UserPasswordChange.as_view(), name="password_change"
    ),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complette/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]