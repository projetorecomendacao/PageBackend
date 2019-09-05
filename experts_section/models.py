from django.db import models

from participant_section.models import Participant


class Expertise (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class Expert (models.Model):
    name = models.CharField(max_length=60)
    expertises = models.ManyToManyField(Expertise, related_name='experts')
    contacts = models.ManyToManyField(Participant, related_name='experts')

    class Meta:
        ordering = ['id']

