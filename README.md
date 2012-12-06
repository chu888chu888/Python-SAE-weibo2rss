# Weibo2rss #

## 概述 ##

Weibo2rss是一个通过Django实现的微博小工具，主要功能实现微博timeline与favorites输出为RSS。

程序员T(就是我,以下用T代替)一直想翻过伟大的GFW更新Twitter，所以想了一个主意，把T更新的新浪微博通过某种方式转换为RSS，然后用IFTTT或者Google feedburner同步到Twitter。

以前T一直用着[水脉烟香](http://ishow.sinaapp.com/rss.php)提供的RSS生成器来同步到Twitter，8月的某一天水脉烟香停掉了这个RSS生成器，然后10月的某一天，又从新开放了，但是开始收费，这么小的东西也能收费？我也不能理解。
10月的时候T开始学习python和Django，既然有需求，那不如学以致用，所有有了Weibo2rss这个项目。12月IFTTT可以绑定影响笔记，所以T又实现了收藏微博的RSS，这样就可以把微博直接收藏到印象笔记了。

T的新浪微博: [@Timmy](http://weibo.com/u/2283077624) 请私信联系
[Weibo2rss demo](http://pythonweibo.sinaapp.com)
***

## 部署 ##

Weibo2rss是部署到SAE上的APP，你需要在SAE上新建一个python app，到新浪微博开放平台申请一个APP。对以下文件作对应修改。

*  config.yaml

> name: ''xxxx'' # 这里写你在SAE上申请的APP name

*  weibo2rss/weibotimeline.py

> APP_KEY = 'xxxx' # 你申请的微博APP_KEY
> APP_SECRET = 'xxxx' # 你申请的微博APP_SECRET
> CALLBACK_URL = 'http://xxxx/callback' # 你的网址回调页，需与微博开放平台上设置的地址一致

导入数据库：在SAE上初始化mysql后，导入weibo2rss.sql里保存的sql语句。

SAE上创建一个版本，把修改好的代码svn上传到该版本上，就完成部署了。
----

## 开发说明 ##

### 开发环境 ###

Weibo python SDK
Django

### 设计思路 ###

*  主页登录微博授权
*  授权回调后，保存用户id,access_token,expires_in到数据库，如已存在该id则更新数据，回调页面返回用户timeline与favorites rss的链接地址。
*  RSS地址输入用户id查找数据库获取access_token,expires_in，调用微博API接口获取数据并渲染到xml模版输出RSS内容
*  补充了一个clean视图函数用于每个星期定时清理授权过期的access_token，config.yaml保持有定时配置
