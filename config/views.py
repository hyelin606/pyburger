# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse

# def main(request):
     # return HttpResponse("안녕하세요, pyburger입니다.")

# def burger_list(request):
     # return HttpResponse("pyburger의 햄버거 목록입니다.")

from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers": burgers,
    }

    return render(request, "burger_list.html", context)

def burger_search(request):
    # print(request.GET)
    keyword = request.GET.get("keyword")
    # print(keyword)
    # burgers = Burger.objects.filter(name__contains=keyword)
    # print(burgers)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)

    else:
        burgers = Burger.objects.none()

    context = {
        "burgers": burgers,
    }

    return render(request, "burger_search.html.", context)
    

