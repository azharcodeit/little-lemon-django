from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
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