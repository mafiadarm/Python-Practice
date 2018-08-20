from django.urls import re_path
from . import views

urlpatterns = [
    re_path("^register/$", views.register),
    re_path("^register_handle/$", views.register_handle),
    re_path("^login/$", views.login),
    re_path("^register_exist/$", views.register_exist),
    re_path("^login_handle/$", views.login_handle),
    re_path("^info/$", views.info),
    re_path("^order/$", views.order),
    re_path("^site/$", views.site),
    re_path("^logout/$", views.logout),
]