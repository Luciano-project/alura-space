from django.contrib import admin
from apps.gallery.models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda","categoria", "foto", "publicada", "usuario")
    list_display_links = ("id","nome","usuario",)
    list_filter = ("nome", "categoria", "usuario",)
    list_editable = ("publicada", )
    search_fields = ("id", "nome", "legenda", "categoria", "foto", "publicada", "usuario")
    readonly_fields = ("data_fotografia",)

    list_per_page = 10

admin.site.register(Fotografia, FotografiaAdmin)