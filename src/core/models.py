from django.db import models

from simple_history.models import HistoricalRecords

from . import choices


class ModelBase(models.Model):
    
    criado = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True,
        null=True,
        blank=True
    )
    modificado = models.DateTimeField(
        verbose_name='Data de Modificação',
        auto_now=True,
        null=True,
        blank=True
    )
    origem_dados = models.IntegerField(
        verbose_name='Origem dos Dados',
        choices=choices.C_TIPO_ORIGEM_DADOS,
        default=choices.ORIGEM_DADOS_MANUAL,
        null=True,
        blank=True
    )
    
    history = HistoricalRecords(inherit=True)
    

    class Meta:
        abstract = True
