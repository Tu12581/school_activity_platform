"""
URL configuration for school_activity_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
# from app import views
from app.views import *
from app.views import login, admin, activities

urlpatterns = [
    #    path("admin/", admin.site.urls),
    path("login/",login.login),
    path("register/",login.register),
    path("index/<int:user_id>/",login.index, name="index"),
    # 这里的动态参数是传递给视图函数的，给视图函数使用
    path('logout/', login.logout, name='logout'), #退出
    path('test/', login.test),
    path("activity_browse/",admin.activity_browse),
    path('activity_manage/', admin.activity_manage),
    path('activity/',activities.activity_detail, name='activity_detail'),
    # 当用户访问 /activity/ 时，activity_view 视图会检查是否有 id 查询参数。
    # 如果没有 id 参数，视图会渲染 activity_list.html，显示所有活动的列表。
    # 如果用户点击某个活动的链接（例如 /activity/?id=1），视图会根据 id 查询数据库，获取对应的活动对象，并渲染 activity_detail.html，显示该活动的详细信息。
    path('del_activity/',admin.del_activity, name='del_activity'),
    path('add_activity/',admin.add_activity, name='add_activity'),
    path("main_page/",activities.main_page),
]
