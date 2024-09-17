from django.shortcuts import render, HttpResponse
# from django.http.response import HttpResponse

# Create your views here.
def show(request):
    return HttpResponse("Hello Page One")
