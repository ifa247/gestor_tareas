from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from .forms import CustomSignupForm

# Registro de usuario
def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm
# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenido {user.username} 👋")
            return redirect('task_list')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamenteveb")
    return redirect('login')
