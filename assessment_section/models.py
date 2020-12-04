from django.db import models
from experts_section.models import *


class DemandsProblems (models.Model):
    description = models.CharField("Descrição do Problema ou Demanda",max_length=100)
    class Meta:
        ordering = ['id']


class Actions(models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class Services(models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class Goals(models.Model):
    CHOICES = [
        ["C", "Curto"],
        ["M", "Médio"],
        ["L","Longo"]
    ]
    term = models.CharField("Prazo de implementação", max_length=1, default="C", choices=CHOICES)
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']

class ActionsPlanning (models.Model):
    demand_problem = models.ForeignKey(DemandsProblems,verbose_name="Demanda/Problema", on_delete=models.CASCADE)
    goals = models.ManyToManyField(Goals,verbose_name="Establecimento de Metas")
    actions = models.ManyToManyField(Actions,verbose_name='Ações')
    services = models.ManyToManyField(Services,verbose_name='Serviços')

    class Meta:
        ordering = ['id']


class ActionImplementationCoordenation(models.Model):
    data = models.DateField("Data")
    action = models.ForeignKey(Actions, verbose_name="Ação Implementada",on_delete=models.CASCADE)
    expertise = models.ManyToManyField(Expertise,verbose_name="Profissionais Envolvidos")
    services = models.ManyToManyField(Services,verbose_name="Serviços realizados")

    class Meta:
        ordering = ['id']

class ReassessmentControl (models.Model):
    data = models.DateField("Data")
    action_result = models.CharField("Ação/resultado",max_length=100,null=True)
    adequacy = models.CharField("Adequação/Metas/Ações",max_length=100,null=True)

    class Meta:
        ordering = ['id']

class DemandMap(models.Model):
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    dm3_unmet_demands = models.TextField('O(a) idoso(a) apresenta outras demandas não contempladas no mapa? Se sim, especificar:',null=True, blank=True)
    gerontologist_assessment =  models.TextField('Avaliação do Gerontólogo',null=True, blank=True)
    demands_problems = models.TextField('Demandas/Problemas',null=True, blank=True)
    goals = models.TextField('Metas',null=True, blank=True)
    actions_organization = models.TextField('Organização das Ações',null=True, blank=True)
    coordenation_implementation = models.TextField('Coordenação / Implementação',null=True, blank=True)
    control = models.TextField('Controle / Reavaliação',null=True, blank=True)
#    actions_planning = models.ForeignKey(ActionsPlanning, on_delete=models.CASCADE, verbose_name="Planejamento das Ações")
#    actions_implementation_coordenation : models.ForeignKey(ActionImplementationCoordenation, on_delete=models.CASCADE,verbose_name="Coordenação e Implementação das Ações")
#    reassessment_control : models.ForeignKey(ActionsPlanning, on_delete=models.CASCADE,verbose_name="Planejamento das Ações")

    def escores(self):
        pass

    def d1_domain_contribution_calculation(self):
        pass

    def d2_dimension_contribution_calculation(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Mapa das Demandas'
        verbose_name_plural = 'Mapa das Demandas'
