from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
import requests
from django.contrib import messages
# import models
from app.models import Users, Activity
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):  # 注册界面
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        role = request.POST['register_choice']
        if not username:
            messages.error(request, '用户名不能为空喵')
            # 回到开始的注册界面
            return render(request,"register.html")
        if not password:
            messages.error(request, '密码不能为空喵')
            return render(request, "register.html")
        user = Users()
        user.username = username
        user.password = password
        user.role = role
        user.save()
    return render(request,"register.html")

def login(request):  # 登录界面
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        role = request.POST['login_choice']
        # 用authenticate函数进行身份验证
        user = auth.authenticate(request, username=username, role=role, password=password)
        if user is not None:  # 能在数据库中找到对应用户
            # 管理员登录后界面
            if role == 'admin':
                auth.login(request, user, backend=None)
                return redirect(f'/index/{user.user_id}/')
            # 普通用户登陆后界面
            else:
                auth.login(request, user, backend=None)
                return redirect(f'/index/{user.user_id}/')
        """try:  # 使用try保证找不到用户名的情况下程序也能正常运行
            user = Users.objects.get(user_name=username, role=role)
            if user.password == password:
                if request.POST['login_choice'] == "admin":
                    # 使用session会话来存储用户的登录状态，便于后续使用
                    request.session['is_login'] = True
                    request.session['user_role'] = user.role
                    request.session['username'] = user.user_name
                    return redirect('/index/')
                else:
                    # 使用session会话来存储用户的登录状态，便于后续使用
                    request.session['is_login'] = True
                    request.session['user_role'] = user.role
                    request.session['username'] = user.user_name
                    return redirect('/index/')
            else:
                messages.error(request, '密码不正确喵')
                return render(request, "login.html")
        except:
            messages.error(request, "找不到对应的用户喵")
            return render(request, "login.html")"""
    return render(request,"login.html")

@login_required
# 路由保证仅登录用户可访问该界面
def index(request, user_id = None):
    user = request.user
    name = user.user_name
    print(request.user.is_authenticated)
    print(name)
    print(user_id)
    return render(request, 'index.html', {'name': name})


'''    用户退出'''
def logout(request):
    auth.logout(request)
    # 退出登录状态
    return redirect('/login/') #退出后，页面跳转至登录界面

def test(request):
    return render(request, 'index.html')