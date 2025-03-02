from datetime import datetime

from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
import requests
from django.contrib import messages
# import models
from app.models import Users, Activity, AcReq,ShenheRecord
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
@login_required
def activity_browse(request): # 查看活动发布

    return render(request,"activity_browse.html")

# 该界面用于管理员管理活动
@login_required
def activity_manage(request):
    ac = Activity.objects.all()
    # 一条十页记录
    paginator = Paginator(ac, 10)
    # 当前显示的页码
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "activity_list.html", {'page_obj': page_obj})

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
@login_required
def del_activity(request):
    ac_id = request.GET['id']
    Activity.objects.filter(ac_id=ac_id).delete() # 在数据库中删除这条数据记录
    return render(request, "activity_list.html")

# 用于管理员修改活动
@login_required
def edit_activity(request):
    ac_id = request.GET['id']
    ac = Activity.objects.get(ac_id=ac_id)
    if request.method == 'GET':

        return render(request, "activity_browse.html", {'activity': ac})
    else:
        activity_name = request.POST['activity_name']
        activity_desc = request.POST['activity_content']
        activity_time = request.POST['activity_time']
        activity_place = request.POST['activity_place']
        ac.objects.filter(ac_id=ac_id).update(ac_place=activity_place)
        ac.objects.filter(ac_id=ac_id).update(ac_pe=activity_name)
        ac.objects.filter(ac_id=ac_id).update(ac_time=activity_time)
        ac.objects.filter(ac_id=ac_id).update(acdesc=activity_desc)
        messages.add_message(request, messages.SUCCESS, '更新完成喵~')
        return render(request, "activity_browse.html")


# 管理员审核活动申请
@login_required
def apply_examine(request):
    if request.user.role == "admin":
        # 直接建立两个数据库，一个用于存储已经审核过的数据，一个用于存储还未审核的申请
        # 当管理员较多的时候怎么去解决审核多少条，是否重复审核的问题，申请如何呈现在管理员面前，多少条？
        # 目前为数据库直接查找数据库未审核的记录
        # 需使用redis数据库优化缓存,并使用分布式锁锁定审核
        # assigned_reqs = AcReq.objects.filter(is_req='pending')
        assigned_reqs = AcReq.objects.filter()
        # 分页处理，每页显示 10 条记录
        paginator = Paginator(assigned_reqs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # page_obj可以算一个带函数的列表，存储了当前页码，直接使用page in page_obj可以遍历该page_obj中的页码
        return render(request, "apply_examine.html", {'req':assigned_reqs, 'page_obj': page_obj})
    else:
        return HttpResponse("您没有权限查看这个喵")

# 同意活动申请
@login_required
def approve_apply(request):
    req_id = request.GET['id']
    AcReq.objects.filter(req_id=req_id).update(is_req="approved")
    record = ShenheRecord()
    record.req_id = req_id
    record.exam_date = datetime.now()
    record.exam_exp = "approved"
    record.admin_id = request.user.user_id
    record.save()
    return redirect("/apply_examine/")


# 拒绝活动申请
@login_required
def reject_apply(request):
    req_id = request.GET['id']
    AcReq.objects.filter(req_id=req_id).update(is_req="rejected")
    record = ShenheRecord()
    record.req_id = req_id
    record.exam_date = datetime.now()
    record.exam_exp = "rejected"
    record.admin_id = request.user.user_id
    record.save()
    return redirect("/apply_examine/")


# 查看所有审核记录
@login_required
def examine_record_list(request):
    if request.user.role == "admin":
        record = ShenheRecord.objects.all()
        paginator = Paginator(record, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "examine_record_list.html", {'page_obj': page_obj})
    else:
        return HttpResponse("这是机密，您没有权限查看喵")
