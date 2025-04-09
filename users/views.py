from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.forms import RegisterUserForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from users.forms import ProfileUserForm, UserPasswordChangeForm


# def login_user(request):
#     if request.method == "POST":
#         form=LoginUserForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             user=authenticate(request, username=cd['username'],
#             password=cd["password"])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("women:index"))
#     else:
#         form=LoginUserForm()
#     #return HttpResponse('login')
#     context={
#         "form":form,
#     }
#     return render(request, "users/login_user.html", context)
class LoginUser(LoginView):
    # form_class=AuthenticationForm
    form_class = LoginUserForm
    template_name = "users/login_user.html"
    extra_context = {"title": "Authorization"}

    # def get_success_url(self):  # для перенаправления или этот метод или в settings.py
    #     return reverse_lazy("women:index")


# при использовании LOGOUT_REDIRECT_URL функция не нужна
# def logout_user(request):
#     logout(request)
#     #return HttpResponse('logout')
#     return HttpResponseRedirect(reverse("users:login_user"))

# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extrs_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login_user")


# def profile(request):
#     context={


#     }
#     return render(request,"users/profile.html", context)
class ProfileUser(
    LoginRequiredMixin, UpdateView
):  # LoginRequiredMixin-доступ к профилю у авторизованных
    # для обновления профиля
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    extra_context = {"title": "Профиль пользователя"}

    def get_success_url(self):
        # return reverse_lazy("users:profile", args=[self.request.user.pk])
        return reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


# смена пароля -password change
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
