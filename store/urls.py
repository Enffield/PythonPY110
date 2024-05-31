from django.urls import path
from .views import products_view, shop_view, products_view_1, products_page_view

urlpatterns = [
    path('product/', products_view),
    path('', shop_view),
    path('product_1/', products_view_1),
    path('product/<slug:page>.html/', products_page_view),
]

