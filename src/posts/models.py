from django.db import models
from django.contrib.auth.models import User


from core.models import ModelBase
from tags.models import Tag
from . import choices

class Post(ModelBase):
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Autor'
    )
    titulo = models.CharField(
        verbose_name='Título',
        max_length=200
    )
    conteudo = models.TextField(
        verbose_name='Conteúdo',
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name='Slug'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        verbose_name='Tags'
    )
    status = models.IntegerField(
        verbose_name='Status',
        choices=choices.C_TIPO_DE_STATUS,
        default=choices.STATUS_RASCUNHO
    )
    
    class Meta:
        ordering = ['-modificado']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo
