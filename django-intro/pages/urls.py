from django.urls import path
from . import views
# articles/urls.py

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
