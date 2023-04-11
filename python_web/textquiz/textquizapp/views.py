from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("TextQuizApp")


def creat(request):
    return HttpResponse("Creat")


def read(request, id):
    return HttpResponse("Read"+id)
