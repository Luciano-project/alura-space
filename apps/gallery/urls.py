from django.urls import path
from apps.gallery.views import \
    index, buscar, imagem, nova_imagem, editar_imagem, deletar_imagem, filtro

urlpatterns = [
    path('', index, name="index"),
    path('imagem/<int:fotografia_id>', imagem, name="imagem"),
    path('buscar', buscar, name="buscar"),
    path('nova-imagem', nova_imagem, name="nova_imagem"),
    path('editar-imagem/<int:fotografia_id>', editar_imagem, name="editar_imagem"),
    path('deletar-imagem/<int:fotografia_id>', deletar_imagem, name="deletar_imagem"),
    path('filtro/<str:categoria>', filtro, name="filtro"),
]
