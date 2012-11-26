# -*- coding: utf-8 -*-

from weibo import APIClient

APP_KEY = '4289845311'
APP_SECRET = 'c80a1f9e844bb399cb722e8bff3d35e4'
CALLBACK_URL = 'http://zhu327.diandian.com/callback'


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

def geturl():
	url = client.get_authorize_url()

	print url

def give(code):
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in

	client.set_access_token(access_token, expires_in)

	return client.statuses.user_timeline.get(count=1)

