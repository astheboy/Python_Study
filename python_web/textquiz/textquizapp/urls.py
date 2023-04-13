
from django.urls import path
from textquizapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creat/<str:keyword>', views.creat, name='creat'),
    path('read/<int:id>', views.read, name='read'),
    path('submit_message/', views.submit_message, name='submit_message'),
    path('creat/submit_message/', views.submit_message, name='submit_message'),
]
