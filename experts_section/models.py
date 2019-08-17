from django.db import models

class Expertise (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class Expert (models.Model):
    name = models.CharField(max_length=60)
    expertises = models.ManyToManyField(Expertise)

    class Meta:
        ordering = ['id']

