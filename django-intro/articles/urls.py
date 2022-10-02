from django.urls import path
from . import views
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dtl/', views.dtl, name='dtl'),
    path('greeting/', views.greeting, name='greeting'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),  
    path('hello/<str:name>', views.hello, name='hello'), 
]
