from django.shortcuts import render
from django.http import HttpResponse

def core_v(request):
    return HttpResponse('core')
