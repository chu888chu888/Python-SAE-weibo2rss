#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient

__version__ = '0.1'
__author__ = 'zhu327'

APP_KEY = 'xxx'    # 填写申请的APP_KEY
APP_SECRET = 'xxx'    # 填写申请的APP_SECRET
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

''' posttext.py 调用weibo SDk 命令发微博 '''

# 获取微博授权，手动操作
def getclient():
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()

	print url    # 浏览器打开该url，取得code='xxx'类似的code输入

	code = raw_input('Enter code >')

	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in

	client.set_access_token(access_token, expires_in)

	return client

# 发微博
def posttext(client):
	text = raw_input('Enter text to post >')
	utext = unicode(text, "UTF-8")
	client.statuses.update.post(status=utext)

if __name__ == '__main__':
    client = getclient()
    posttext(client)
