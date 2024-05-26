from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from app_datetime.views import new_click, get_file
from project_my.views import products_view, shop_view


def return_value(request):
    return HttpResponse('Тебя люблю)')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ses/', return_value),
    path('lera/', new_click),
    path('cat/', get_file),
    path('product/', products_view),
    path('', shop_view),
]
