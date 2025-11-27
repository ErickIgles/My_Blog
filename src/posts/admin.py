from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'autor',
        'titulo',
        'conteudo',
        'get_tags',
        'criado',
        'modificado',
        'origem_dados'
    ]
    
    list_display_links = [
        'autor',
        'titulo'
    ]
    
    search_fields = [
        'autor',
        'titulo'
    ]
    
    list_filter = [
        'autor',
    ]
    
    
    def get_tags(self, obj):
        return ', '.join([tag.nome for tag in obj.tags.all()])

    get_tags.short_description = 'Tags'
    
    prepopulated_fields = {'slug': ('titulo',)}
