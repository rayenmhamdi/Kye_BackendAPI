from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def example_http(request):
    return HttpResponse("hello from your example app")