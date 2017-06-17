# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#数据库设计

#用户表

class User(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30,unique=True,blank=True, null=True, verbose_name=u'用户名')
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True,null=True, verbose_name=u'用户头像')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name=u'邮箱地址')
    brief = models.CharField(max_length=140, verbose_name=u'简介', blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

#文章表
class Article(models.Model):
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.content

#评论
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')


    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.content


