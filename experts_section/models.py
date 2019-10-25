from django.db import models

from participant_section.models import Participant


class Expertise (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class Expert (models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    expertises = models.ManyToManyField(Expertise, related_name='experts', blank=True)
    contacts = models.ManyToManyField(Participant, related_name='experts2', blank=True)

    class Meta:
        ordering = ['id']

class Gerontologist (models.Model):
    name = models.CharField(max_length=30)
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, null=True, verbose_name = 'Especialista')

    class Meta:
        ordering = ['id']