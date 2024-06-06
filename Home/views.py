from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'Home/Home.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == 'root' and password == "123":
            return render(request, 'menu/menu.html')
        else:
            return render(request, 'Home/Home.html', {"error_msg": "用户名或密码错误"})


def register(request):
    return render(request, 'Home/register.html')


def Home_sheller(request):
    return render(request, 'Home/Home_sheller.html')
