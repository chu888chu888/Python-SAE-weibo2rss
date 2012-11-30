# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from weibo2rss.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weibo2rss.views.home', name='home'),
    # url(r'^weibo2rss/', include('weibo2rss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', getfeedurl),    # 主页
    url(r'^back/$', callback),     # 返回页，返回rss链接
    url(r'^callback/$', callback),     # 微博授权返回页
    url(r'^feed/(?P<usrid>\d+)/$', getfeed),    # 微博feed页，通过user id获取
)
