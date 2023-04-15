
from django.urls import path
from textquizapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creat/<str:keyword>', views.creat, name='creat'),
    path('creat/creat/', views.creat, name='creat'),
    path('creat/', views.creat, name='creat'),
    path('word/<str:word>', views.word, name='word'),
]
