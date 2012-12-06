# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404
import weibo
from weibotimeline import *
from models import AccessToken

'''module views django 视图函数'''

def getfeedurl(request):
    '''主页获取微博授权地址'''
    url = geturl()
    return render_to_response('index.html', locals())

def callback(request):
    '''微博授权回调页，更新或保存access token到数据库，返回rss地址'''
    if 'code' in request.GET and request.GET['code']:
        code = request.GET['code']
        try:
            access_token, expires_in, uid = getoken(code)
            t = AccessToken.objects.filter(uid=uid)
            if t:
                t[0].access_token = access_token
                t[0].expires_in = expires_in
                t[0].save()
            else:
                AccessToken.objects.create(uid=uid, access_token=access_token, expires_in=expires_in)
        except weibo.APIError:
            raise Http404
    else:
        raise Http404
    return render_to_response('back.html', locals())

def timeline(request, uid):

    '''通过uid获取对应的access token，获取微博timeline'''
    try:
        uid = int(uid)
        token = AccessToken()
        t = AccessToken.objects.get(uid=uid)
        user = getuid(t.access_token, t.expires_in, t.uid)
        statuses = gettimeline(t.access_token, t.expires_in)
    except (ValueError, AccessToken.DoesNotExist, weibo.APIError,):
        raise Http404

    # 模版只支持False判断，对于没有图片的微博补全'original_pic'，改写时间格式
    for tweet in statuses:
        if not('original_pic' in tweet.keys()):
            tweet['original_pic'] = False

        time = tweet.created_at.split(' ')
        tweet.created_at = ' '.join([time[2],time[1],time[5],time[3],time[4]])

    appkey = APP_KEY

    return render_to_response('feed.xml', locals(), mimetype="application/xml")

def favorites(request, uid):

    '''通过uid获取对应的access token，获取微博favorites'''
    try:
        uid = int(uid)
        token = AccessToken()
        t = AccessToken.objects.get(uid=uid)
        user = getuid(t.access_token, t.expires_in, t.uid)
        favorites = getfavorites(t.access_token, t.expires_in)
    except (ValueError, AccessToken.DoesNotExist, weibo.APIError,):
        raise Http404

    # 模版只支持False判断，对于没有图片的微博补全'original_pic'，改写时间格式
    for tweet in favorites:
        if not('original_pic' in tweet.status.keys()):
            tweet.status['original_pic'] = False

        time = tweet.favorited_time.split(' ')
        tweet.favorited_time = ' '.join([time[2],time[1],time[5],time[3],time[4]])

    appkey = APP_KEY

    return render_to_response('favorites.xml', locals(), mimetype="application/xml")

def clean(request):
    '''清理数据库中保存的过期授权，用于定时任务'''
    tl = AccessToken.objects.all()
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    for t in tl:
        client.set_access_token(t.access_token, t.expires_in)
        if client.is_expires():
            t.delete()
    return render_to_response('base.html')