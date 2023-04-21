
from django.urls import path
from textquizapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<str:keyword>', views.create, name='create'),
    path('create/create/', views.create, name='create'),
    path('create/', views.create, name='create'),
    path('word/<str:word>', views.get_word_meaning, name='word'),
]
