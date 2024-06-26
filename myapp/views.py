from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello")

def products(request):
    products = ["iphone","android","mac"]
    return HttpResponse(products)

