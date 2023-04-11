
from django.urls import path
from textquizapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creat/', views.creat, name='creat'),
    path('read/<id>', views.read, name='read')
]
