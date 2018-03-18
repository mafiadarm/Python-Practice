"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from app import views

# 在主页尾巴上加的值对应路径，用正则匹配，返回views里面的函数[尾巴值，函数，显示名字]
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views.home, name="home"),
    path("artists", views.artists, name="artists"),
    path("artists/create", views.artistcreate, name="artistcreate"),
    re_path(r"^artists/(?P<name>[A-Za-z]+)$", views.artistdetails, name="artistdetails"),
    re_path(r"^artists/(?P<id>\d+)$", views.artistid, name="artistid"),

]

