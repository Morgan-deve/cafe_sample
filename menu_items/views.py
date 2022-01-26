from django.shortcuts import render
from django.http import HttpResponse

def menu_item_v(request):
    return HttpResponse('menu_item')
