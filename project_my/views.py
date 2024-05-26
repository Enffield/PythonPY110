from django.shortcuts import render
from django.http import JsonResponse
from project_my.models import DATABASE
from django.http import HttpResponse

def products_view(request):
    if request.method == "GET":
        return JsonResponse(DATABASE)

def shop_view(request):
    if request.method == "GET":
        with open('project_my/shop.html', encoding="utf-8") as f:
            data = f.read()
        return HttpResponse(data)
