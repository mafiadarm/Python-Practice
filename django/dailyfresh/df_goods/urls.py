from django.urls import re_path
from . import views

urlpatterns = [
    re_path("^$", views.index),
    re_path("^list(\d+)_(\d+)_(\d+)/$", views.goods_list),
    re_path("^(\d+)/$", views.detail),
]
