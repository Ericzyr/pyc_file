#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'test_django.views.test_view')
]