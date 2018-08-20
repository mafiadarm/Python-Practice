# coding=utf-8
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from . import user_decorator
from ..df_goods.models import *


# Create your views here.

def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    post = request.POST
    uname = post["user_name"]
    upwd = post["pwd"]
    upwd2 = post["cpwd"]
    uemail = post["email"]

    count = UserInfo.objects.filter(uname=uname).count()

    if upwd != upwd2 or count >= 1:
        return redirect("/user/register/")

    s1 = sha1(upwd.encode())
    upwd3 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    return redirect("/user/login/")


def register_exist(request):
    uname = request.GET.get("uname")
    count = UserInfo.objects.filter(uname=uname).count()
    print(count)
    return JsonResponse({"count": count})


def login(request):
    uname = request.COOKIES.get("uname", "")
    context = {"title": "user login", "error_name": 0, "error_pwd": 0, "uname": uname}
    return render(request, "df_user/login.html", context)


def login_handle(request):
    post = request.POST
    uname = post.get("username")
    upwd = post.get("pwd")
    jizhu = post.get("jizhu", 0)

    users = UserInfo.objects.filter(uname=uname)  # []

    if len(users) == 1:
        print("user login")
        s1 = sha1(upwd.encode())
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect("/user/info")

            if jizhu != 0:
                red.set_cookie("uname", uname)
            else:
                red.set_cookie("uname", "", max_age=-1)
            request.session["user_id"] = users[0].id
            request.session["user_name"] = uname
            return red
        else:
            context = {"title": "user login", "error_name": 0, "error_pwd": 1, "uname": uname, "uwpd": upwd, }
    else:
        context = {"title": "user login", "error_name": 0, "error_pwd": 1, "uname": uname, "uwpd": upwd, }
        return render(request, "df_user/login.html", context)


@user_decorator.login
def info(request):
    in_fo = UserInfo.objects.get(id=request.session["user_id"])
    user_phone = "No" if not in_fo.uphone else in_fo.uphone
    user_address = "No" if in_fo.uaddress else in_fo.uaddress
    user_email = "No" if in_fo.uemail else in_fo.uemail

    # 最近浏览记录
    goods_ids = request.COOKIES.get("goods_ids", "")
    goods_ids1 = goods_ids.split(",")
    goods_list = []

    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {"title": "用户中心",
               "user_email": user_email,
               "user_name": request.session["user_name"],
               "user_phone": user_phone,
               "user_address": user_address}
    return render(request, "df_user/user_center_info.html", context)


@user_decorator.login
def order(request):
    context = {"title": "user center"}
    return render(request, "df_user/user_center_order.html", context)


@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session["user_id"])
    if request.method == "POST":
        post = request.POST
        user.ushou = post.get("shou")
        user.uaddress = post.get("uaddress")
        user.uyoubian = post.get("uyoubian")
        user.uphone = post.get("uphone")
        user.save()
    context = {
        "title": "user center",
        "user": user,
        "user_address": user.ushou + user.uaddress + user.uphone + user.uyoubian,
        "page_name": 1,
    }
    return render(request, "df_user/user_center_site.html", context)


def logout(request):
    request.session.flush()
    return redirect("/")