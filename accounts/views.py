from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .create_form import CreateUser
from .decorators import unauthenticated_user
from .models import User

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
            return redirect('accounts:register')
        else:
            messages.info(request, "Username or password incorrect")
            return render(request, 'account_actions/login.html')


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
        return redirect('accounts:login')


class Dashboard(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {
            'user_info': user,
        }
        return render(request, 'dashboard/dashboard.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class UploadProfileImg(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        img = request.FILES['img']
        if self.__validate(img):
            obj = User.objects.get(id=request.user.id)
            obj.profile_pic = request.FILES['img']
            obj.save()
            return JsonResponse({'msg': 'Success'}, status=200)
        else:
            return JsonResponse({'msg': 'Invalid file'}, status=404)

    def __validate(self, img_name):
        VALID_EXTENSIONS = ['jpg', 'jpeg', 'png']
        if str(img_name).split('.')[-1] in VALID_EXTENSIONS:
            return True
        return False
