from django.db import models


class Diseases(models.Model):
    description = models.TextField()


class Medication(models.Model):
    description = models.TextField()
