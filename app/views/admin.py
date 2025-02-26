from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
import requests
from django.contrib import messages
# import models
from app.models import Users, Activity
from django.contrib import auth
from django.contrib.auth.decorators import login_required
@login_required
def activity_browse(request): # 查看活动发布

    return render(request,"activity_browse.html")

# 该界面用于管理员管理活动
@login_required
def activity_manage(request):
    ac = Activity.objects.all()
    return render(request, "activity_list.html", {'activity': ac})

# 添加活动
@login_required
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
            messages.add_message(request, messages.SUCCESS, '添加成功！')
        return render(request,"activity_browse.html")
    else:
        messages.error(request, '您没有这个权限喵')
        return render(request,"activity_browse.html")

# 用于管理活动的删除
def del_activity(request):
    ac = Activity.objects.all()
    return render(request, "activity_list.html", {'activity': ac})