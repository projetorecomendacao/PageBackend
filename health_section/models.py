from django.db import models


class Diseases(models.Model):
    description = models.TextField()

class TherapeuticClass(models.Model):
    description = models.TextField()

class Medicines(models.Model):
    description = models.TextField()

class HealthProblems(models.Model):
    description = models.TextField()

class Fractures(models.Model):
    descripton = models.CharField(max_length=60)
