from django.contrib import admin
from .models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda","categoria", "foto", "publicada")
    list_display_links = ("id","nome",)
    list_filter = ("nome", "categoria",)
    list_editable = ("publicada", )
    search_fields = ("id", "nome", "legenda", "categoria", "foto", "publicada")
    readonly_fields = ("data_fotografia",)

    list_per_page = 10

admin.site.register(Fotografia, FotografiaAdmin)