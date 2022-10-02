from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def dtl(request):
    name = 'ABCEFGHIJKLMNO'
    context = {
        'name' : name,
        'age' : 30,
        'foods' : ['apple', 'banana', 'pizza','chicken', 'hamburger']
    }
    # return render(request, 'dtl.html', {'name':'phang'})
    return render(request, 'articles/dtl.html', context)

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name' : 'Alice'
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/greeting.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    value = request.GET.get('search')
    name = 'phang'
    context = {
        'value' : value,
        'name' : name
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/catch.html', context)