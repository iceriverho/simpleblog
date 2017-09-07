# -*- coding: utf-8 -*-
# @Time    : 2017/9/7 22:46
# @Author  : vincent.he
# @Email   : iceriverho@qq.com
# @File    : urls.py
# @Software: PyCharm Community Edition

from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.post_list),
]