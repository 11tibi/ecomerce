from django.shortcuts import render
from django.views import View
from .create_form import CreateUser

# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'account_actions/login.html')
    
    def post(self, request):
        pass


class Register(View):
    def get(self, request):
        form = CreateUser()
        context = {'form': form}
        return render(request, 'account_actions/register.html', context)

    def post(self, request):
        form = CreateUser()


class Logout(View):
    pass
