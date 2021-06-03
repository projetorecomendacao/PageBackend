from django.db import models

## Editores são o mesmo do ESM
from esm_program_section.models import EditorProgram

# Create your models here.

class Documento (models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.CharField(max_length=1, default='y')


class ActionsEditor(models.Model):
    # c-create d-delete u-update
    actionType = models.CharField(max_length=1, default="c")
    # 1-documento 2-dimensão 3-domínio 4-questão 
    objectType = models.CharField(max_length=1, default="1")
    #documento
    documento_id = models.IntegerField(null=True, blank=True, default=-1)
    #dimensão
    dimensao_id = models.IntegerField(null=True, blank=True, default=-1)
    #domínio
    dominio_id = models.IntegerField(null=True, blank=True, default=-1)
    #questão
    questao_id = models.IntegerField(null=True, blank=True, default=-1)
    #valor anterior do campo
    anterior = models.JSONField(null=True, blank=True)
    #Editor igual o do ESM
    editor = models.ForeignKey(EditorProgram, on_delete=models.DO_NOTHING, null=True, blank=True)
    #
    actionDate = models.CharField(max_length=50, blank=True, null=True)
    #Data da Ação
    createDate = models.DateTimeField(auto_now_add=True, null=True)