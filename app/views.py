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
def activity_browse(request): # 查看活动发布

    return render(request,"activity_browse.html")

# 该界面用于管理员管理活动
def activity_manage(request):
    ac = Activity.objects.all()
    return render(request, "activity_list.html", {'activity': ac})

# 添加活动
def add_activity(request):
    if request.user.role == "admin":
        if request.method == "POST":
            # 从表单获取活动数据并存储
            activity_name = request.POST['activity_name']
            activity_desc = request.POST['activity_content']
            activity_time = request.POST['activity_time']
            activity_place = request.POST['activity_place']
            activity = Activity()
            activity.ac_pe = activity_name
            activity.ac_time = activity_time
            activity.ac_place = activity_place
            activity.acdesc = activity_desc
            activity.save()
            messages.add_message('添加成功！')
        return render(request,"activity_browse.html")
    else:
        messages.error(request, '您没有这个权限喵')
        return render(request,"activity_browse.html")

# 用于管理活动的删除
def del_activity(request):
    ac = Activity.objects.all()
    return render(request, "activity_list.html", {'activity': ac})
def main_page(request):
    ac = Activity.objects.all()
    return render(request, "activity_list.html", {'activity': ac})
# 用于用户查看活动列表
def user_activity(request):

    return render(request,"activity_browse.html")

# 活动详情
def activity_detail(request):
    # 从查询参数中获取 id
    ac_id = request.GET.get('id')  # 从网页url中获取id参数
    if ac_id:# 如果有传递id
        # 根据 ac_id 获取对应的活动对象
        activity = get_object_or_404(Activity, ac_id=ac_id)
        # 将活动对象传递给模板
        return render(request, 'activity_main.html', {'activity': activity})
    else:
        # 如果没有传递 id，返回所有活动列表
        activities = Activity.objects.all()
        return render(request, 'activity_list.html', {'activity': activities})
