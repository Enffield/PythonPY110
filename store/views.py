from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE
from logic.services import filtering_category
from logic.services import view_in_cart, add_to_cart, remove_from_cart
from django.shortcuts import render

def shop_view(request):
    if request.method == "GET":
        return render(request, 'shop.html')

def cart_view(request):
    if request.method == "GET":
        data = view_in_cart() # TODO Вызвать ответственную за это действие функцию
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


def cart_add_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(request)  # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(request) # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})
# def products_view(request):
#     if request.method == "GET":
#          return JsonResponse(DATABASE)



def products_view(request):
    if request.method == "GET":
        # Обработка id из параметров запроса (уже было реализовано ранее)
        if id_product := request.GET.get("id"):
            if data := DATABASE.get(id_product):
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")

        # Обработка фильтрации из параметров запроса
        category_key = request.GET.get("category")  # Считали 'category'
        if ordering_key := request.GET.get("ordering"): # Если в параметрах есть 'ordering'
            if request.GET.get("reverse").lower() == 'true': # Если в параметрах есть 'ordering' и 'reverse'=True
                data = filtering_category(DATABASE, category_key, ordering_key, True) #  TODO Использовать filtering_category и провести фильтрацию с параметрами category, ordering, reverse=True
            else:  # Если не обнаружили в адресно строке ...&reverse=true , значит reverse=False
                data = filtering_category(DATABASE, category_key, ordering_key) #  TODO Использовать filtering_category и провести фильтрацию с параметрами category, ordering, reverse=False
        else:
            data = DATABASE.get(id_product) #  TODO Использовать filtering_category и провести фильтрацию с параметрами category
        # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})

def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:
                    with open(f'store/products/{page}.html', encoding="utf-8") as file:
                        return HttpResponse(file.read())
        elif isinstance(page, int):
            data = DATABASE.get(str(page))
            if data:
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as file:
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
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False, 'indent': 4})

# def shop_view(request):
#     if request.method == "GET":
#         with open('store/shop.html', encoding="utf-8") as f:
#             data = f.read()
#         return HttpResponse(data)
