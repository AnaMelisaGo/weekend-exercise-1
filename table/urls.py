from django.urls import path
from . import views


urlpatterns = [
    path('pedidos/', views.pedidos, name='pedidos'),
    path('titulo/', views.titulo, name='titulo'),
    path('primer_base', views.primer_base, name='primer_base'),
    path('fusion_columna/', views.fusion_columna, name='fusion_columna'),
]