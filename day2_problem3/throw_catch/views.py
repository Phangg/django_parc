from email import message
from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def first(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'first.html', context)

def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'second.html', context)