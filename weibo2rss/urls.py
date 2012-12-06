# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from weibo2rss.views import *

urlpatterns = patterns('',
    url(r'^$', getfeedurl),    # 主页
    url(r'^callback/$', callback),     # 微博授权返回页
    url(r'^timeline/(?P<uid>\d+)/$', timeline),    # 微博timeline rss页，通过user id获取
    url(r'^favorites/(?P<uid>\d+)/$', favorites),    # 微博favorites rss页，通过user id获取
    url(r'^admin/root/weibo/clean/$', clean),    # 用于定时清理数据库过期授权，非对外页面，清理周期在config.yaml下cron字段定义
)
