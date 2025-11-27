from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.utils.text import slugify

from core.models import ModelBase
from tags.models import Tag
from . import choices


class PostPublicadosManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(status = choices.STATUS_PUBLICADO)
        return qs


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
    
    
    objects = models.Manager()
    publicados = PostPublicadosManager()

    class Meta:
        ordering = ['-modificado']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo
    
    
    def save(self, *args, **kwargs):
        
        if not self.slug and self.titulo:
            base_slug = slugify(self.titulo)
            slug = base_slug
            contador = 1
            
            while Post.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{contador}'
                contador += 1
            self.slug = slug
            
        super().save(*args, **kwargs)
