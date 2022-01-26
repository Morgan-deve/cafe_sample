from django.shortcuts import render
from django.http import HttpResponse

def table_v(request):
    return HttpResponse('table')