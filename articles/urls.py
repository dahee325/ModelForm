from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name='index'),
    
    # Create
    path('create/', views.create, name='create'), 
]