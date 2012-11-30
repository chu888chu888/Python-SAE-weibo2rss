# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404
import datetime
from weibo import APIClient
import weibo
from weibotimeline import *

__version__ = '0.1'
__author__ = 'zhu327'

APP_KEY = 'xxx'    # 填写你的应用APP_KEY
APP_SECRET = 'xxx'    # 填写你的应用 APP_SECRET
CALLBACK_URL = 'xxx'    # 填写你的回调页

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

# 获取微博授权地址
def getfeedurl(request):
    url = client.get_authorize_url()
    return render_to_response('index.html', locals())

# 微博授权回调页，取得feed地址
def callback(request):
    # 从back页GET来的usrid
    if 'usrid' in request.GET and request.GET['usrid']:
        strid = request.GET['usrid']
        try:
            usrid = int(strid)
        except ValueError:
            raise Http404

    # 从callback页GET到的授权CODE
    elif 'code' in request.GET and request.GET['code']:
        code = request.GET['code']
        try:
            r = client.request_access_token(code)
            access_token = r.access_token
            expires_in = r.expires_in

            client.set_access_token(access_token, expires_in)
            usrid = getusrid(client)['id']
        except weibo.APIError:
            raise Http404
    else:
        raise Http404
    return render_to_response('back.html', locals())

# 生成feed
def getfeed(request, usrid):
    try:
        usrid = int(usrid)
    except ValueError:
        raise Http404

    # 获取timeline，user信息
    try:
        user = getusrid(client, usrid)
        statuses = gettimeline(client, usrid)
    except weibo.APIError:
        raise Http404

    # 模版只支持False判断，对于没有图片的微博补全'original_pic'
    for tweet in statuses:
        if not('original_pic' in tweet.keys()):
            tweet['original_pic'] = False

    appkey = APP_KEY
    datenow = datetime.datetime.now()

    return render_to_response('feed.xml', locals())
