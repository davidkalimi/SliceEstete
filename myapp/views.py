from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("Hello, World! This is the properties page.")