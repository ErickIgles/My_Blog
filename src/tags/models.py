from django.db import models

from core.models import ModelBase


class Tag(ModelBase):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=50,
        unique=True
    )
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nome
