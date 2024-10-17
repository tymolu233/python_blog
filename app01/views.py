from django.shortcuts import render, HttpResponse
from app01.utils.get_random_code import random_code
from django.http import JsonResponse
from django import forms

# Create your views here.

# 首页


def index(request):
    img_list = [
        "http://image.fengfengzhidao.com/gvb_1009/20231123092743__1123-h.png",
        "http://image.fengfengzhidao.com/gvb_1009/20231123092743__1123-i.png",
        "http://image.fengfengzhidao.com/gvb_1009/20231019173356__wallhaven-jxl31y.png",
        "http://image.fengfengzhidao.com/gvb_1009/20231019173356__wallhaven-57yr13.jpg",
        "http://image.fengfengzhidao.com/gvb_1009/20231123092743__1123-c.png",
    ]
    return render(request, 'index.html', locals())

def get_random_code(request):
    data, valid_code = random_code()
    request.session['valid_code'] = valid_code
    return HttpResponse(data)

def login(request):
    return render(request, 'login.html')

def sign(request):
    return render(request, 'sign.html')
