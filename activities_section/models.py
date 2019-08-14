from django.db import models


class Characteristic(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Benefit(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Restriction(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Type (models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Activity(models.Model):
    description = models.CharField(max_length=50)

    characteristic = models.ManyToManyField(Characteristic, related_name='activities')
    benefit = models.ManyToManyField(Benefit, related_name='activities')
    restriction = models.ManyToManyField(Restriction, related_name='activities')

    type = models.ManyToManyField(Type, related_name='activities')

    class Meta:
        ordering = ['id']

