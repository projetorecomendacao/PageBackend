from django.contrib.auth.models import User
from django.db import models


class Detail(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['description']

    def __str__ (self):
        return self.description


class Characteristic(Detail):
    pass


class Benefit(Detail):
    pass


class Restriction(Detail):
    pass


class Type (Detail):
    pass


class Activity(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageURL = models.URLField(null=True, blank=True)
    general_activity_objective = models.TextField(null=True)
    author = models.TextField(null=True)

    characteristic = models.ManyToManyField(Characteristic, blank=True, related_name='activities')
    benefit = models.ManyToManyField(Benefit, blank=True, related_name='activities')
    restriction = models.ManyToManyField(Restriction, blank=True, related_name='activities')
    type_activity = models.ManyToManyField(Type, blank=True, related_name='activities')

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.title


