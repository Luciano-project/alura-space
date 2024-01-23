from django.urls import path
from gallery.views import index, buscar, imagem
urlpatterns = [
    path('', index, name="index"),
    path('imagem/<int:fotografia_id>', imagem, name="imagem"),
    path('buscar', buscar, name="buscar"),
]
