from django.shortcuts import render
from django.http import JsonResponse
from .models import DATABASE
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE


def products_page_view(request, page):
    if request.method == "GET":
        for data in DATABASE.values():
            if data['html'] == page:
                with open(f'store/products/{page}.html', encoding="utf-8") as file:
                    return HttpResponse(file.read())
    return HttpResponse(status=404)


def products_view_1(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id:
            if id in DATABASE.keys():
                return JsonResponse(DATABASE[id], json_dumps_params={'ensure_ascii':False, 'indent':4})
            else:
                return HttpResponseNotFound("Данного продукта нет в базе данных")
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii':False, 'indent':4})

def products_view(request):
    if request.method == "GET":
        return JsonResponse(DATABASE)

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()
        return HttpResponse(data)
