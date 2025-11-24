from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'nome',
        'slug',
        'criado',
        'modificado',
        'origem_dados'
    ]
    
    list_display_links = [
        'nome',
        'slug'
    ]
    
    search_fields = (
        'nome',
        'slug',
    )
    
    list_filter = (
        'nome',
        'slug',
    )

