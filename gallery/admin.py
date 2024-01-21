from django.contrib import admin
from .models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "categoria", "foto")
    list_display_links = ("id","nome",)
    list_filter = ("nome", "categoria",)
    search_fields = ("id", "nome", "legenda", "descricao", "categoria", "foto")

    list_per_page = 10

admin.site.register(Fotografia, FotografiaAdmin)