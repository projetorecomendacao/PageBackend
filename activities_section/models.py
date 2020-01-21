from django.db import models


class Detail(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['description']


class Characteristic(Detail):
    pass


class Benefit(Detail):
    pass


class Restriction(Detail):
    pass


class Type (Detail):
    pass


class Activity(models.Model):
    description = models.CharField(max_length=50)

    characteristic = models.ManyToManyField(Characteristic, blank=True, related_name='activities')
    benefit = models.ManyToManyField(Benefit, blank=True, related_name='activities')
    restriction = models.ManyToManyField(Restriction, blank=True, related_name='activities')
    type = models.ManyToManyField(Type, blank=True, related_name='activities')

    class Meta:
        ordering = ['id']

