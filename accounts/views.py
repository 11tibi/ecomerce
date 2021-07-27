from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .create_form import CreateUser
from .decorators import unauthenticated_user


# Create your views here.


class Login(View):
    @method_decorator(unauthenticated_user)
    def get(self, request):
        return render(request, 'account_actions/login.html')

    @method_decorator(unauthenticated_user)
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect('register')
        else:
            messages.info(request, "Username or password incorrect")


class Register(View):
    @method_decorator(unauthenticated_user)
    def get(self, request):
        print(request.user.is_authenticated)
        form = CreateUser()
        context = {'form': form}
        return render(request, 'account_actions/register.html', context)

    @method_decorator(unauthenticated_user)
    def post(self, request):
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {'form': form}
        return render(request, 'account_actions/register.html', context)


class Logout(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        logout(request)
        return redirect('login')
