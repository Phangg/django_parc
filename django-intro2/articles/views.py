from django.shortcuts import render

# Create your views here.

def idx(request):
    context = {
        'name' : 'phang',
        'age' : 30,
        'foods' : ['pizza', 'chicken', 'ramen']
    }
    return render(request, 'idx.html', context)
