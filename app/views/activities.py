from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
import requests
from django.contrib import messages
# import models
from app.models import Users, Activity
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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