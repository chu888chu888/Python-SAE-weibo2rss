# -*- coding: utf-8 -*-

from django.db import models

class AccessToken(models.Model):
    '''定义数据类型uid==用户微博ID，access_token==授权码，expires_in==授权过期时间'''
    uid = models.BigIntegerField()
    access_token = models.CharField(max_length=1000)
    expires_in = models.BigIntegerField()