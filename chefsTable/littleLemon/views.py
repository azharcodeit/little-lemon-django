from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from django.views import View
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.

def hello(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")

def index(request):
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p>
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content)

class MyView(View):
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request>
        return HttpResponse('response to POST request')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer