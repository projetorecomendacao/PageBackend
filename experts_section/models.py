from django.db import models

from participant_section.models import Participant


class Expertise (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class Expert (models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    #2- full, pode ter orientandos 1- orientandos 0 - sem definição
    accesLevel = models.IntegerField(default=0) 
    expertises = models.ManyToManyField(Expertise, related_name='experts', blank=True)
    contacts = models.ManyToManyField(Participant, related_name='experts2', blank=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.name + " - " + self.email

#Tabela que relaciona o orientador com os orientandos.. Criada para a Ruth..
class Orientador (models.Model):
    #Orientador da Relação
    orientador = models.ForeignKey(Expert,on_delete=models.CASCADE,related_name='orientador_expert')
    #Orientado da Relação
    orientando_id = models.ForeignKey(Expert,on_delete=models.CASCADE,related_name='orientando_expert')
    orientando_name = models.CharField(max_length=60, blank=True)
    orientando_email = models.CharField(max_length=60, blank=True)
    dupla_name = models.CharField(max_length=60, blank=True)
    dupla_email = models.CharField(max_length=60, blank=True)
    trio_name = models.CharField(max_length=60, blank=True)
    qtdPages = models.IntegerField(default=0)


class Gerontologist (models.Model):
    name = models.CharField(max_length=30)
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, null=True, verbose_name = 'Especialista')

    class Meta:
        ordering = ['id']