# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import *
# Create your views here.


def index(request):
	articles = Article.objects.all()
	print articles
	return render(request,'info.html',locals())


def login(request):
	return render(request,'login.html')

def publish(request):
	return render(request,'publish.html')


#详情页面
def detail(request):
	id = request.GET.get('id',None)
	article = Article.objects.get(pk=id)
	comment_list = Comment.objects.filter(article_id=id)
	comment_list_num = len(comment_list)
	return render(request,'detail.html',locals())