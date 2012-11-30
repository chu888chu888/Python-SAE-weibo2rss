#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient

__version__ = '0.1'
__author__ = 'zhu327'

# 读取用户最新的10条微博
def gettimeline(client, id=0):
	statuses = client.statuses.user_timeline.get(count=10, feature=1, uid=id)

	return statuses.statuses

# 读取用户微博ID，用users/show接口不行，估计是weibo SDK的问题，只好获取最新的微博来获取ID
def getusrid(client, id=0):
	usrid = client.statuses.user_timeline.get(count=1, feature=1, uid=id)
	return {'id':usrid.statuses[0].user.id, 'name':usrid.statuses[0].user.name}


