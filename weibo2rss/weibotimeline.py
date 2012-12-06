#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient

__version__ = '0.1'
__author__ = 'zhu327'

'''module weibotimeline 定义与微博API相关的系列函数'''

APP_KEY = 'xxxx' # 你申请的微博APP_KEY
APP_SECRET = 'xxxx' # 你申请的微博APP_SECRET
CALLBACK_URL = 'http://xxxx/callback' # 你的网址回调页，需与微博开放平台上设置的地址一致

def geturl():
    '''返回微博授权登录url'''
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    return url

def getoken(code):
    '''回调页返回授权access token'''
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    
    r = client.request_access_token(code)
    return [r.access_token, r.expires_in, int(r.uid)]

def gettimeline(access_token, expires_in):
    '''读取用户最新的10条微博'''
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)
    statuses = client.statuses.user_timeline.get(count=10, feature=1)

    return statuses.statuses

def getfavorites(access_token, expires_in):
    '''读取用户最新收藏的10条微博'''
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)
    favorites = client.favorites.get(count=10)

    return favorites.favorites

def getuid(access_token, expires_in, uid):
    '''读取读取用户微博id,name'''
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)
    usr = client.users.show.get(uid=uid)
    return {'id':usr.id, 'name':usr.name}

