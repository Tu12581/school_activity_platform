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
from app import views

urlpatterns = [
    #    path("admin/", admin.site.urls),
    path("login/",views.login),
    path("register/",views.register),
    path("index/",views.index),
    path("activity_browse/",views.  activity_browse),
    path("main_page/",views.main_page),
    path('logout/', views.logout, name='logout'), #退出
]
