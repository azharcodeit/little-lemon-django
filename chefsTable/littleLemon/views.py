from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def hello(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")

class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request')