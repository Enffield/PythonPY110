from django.shortcuts import render
from django.http import HttpResponse, FileResponse

def new_click(request):
    return HttpResponse('Люблю тебя')

def get_file(request):
    return FileResponse(open('cat.jpg', "rb"))

# Create your views here.
