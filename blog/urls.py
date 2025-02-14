from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agregar-autor/', views.agregar_autor, name="agregar_autor"),
    path('agregar-categoria/', views.agregar_categoria, name="agregar_categoria"),
    path('agregar-post/', views.agregar_post, name="agregar_post"),
    path('buscar-post/', views.buscar_post, name="buscar_post"),
]
