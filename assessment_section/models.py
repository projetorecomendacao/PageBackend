from django.db import models
from experts_section.models import Expertise, Expert


class DemandsProblems (models.Model):
    description = models.CharField(max_length=60)

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
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class AssessmentsControl(models.Model):
    data = models.DateField()
    results = models.TextField()
    adequacy = models.TextField()

    class Meta:
        ordering = ['id']


class ExpertAssessment(models.Model):
    description = models.TextField()
    actions = models.ManyToManyField(Actions, through='ActionsImplementation')

    class Meta:
        ordering = ['id']


class ActionsImplementation(models.Model):
    data = models.DateField()
    actions = models.ForeignKey(Actions, on_delete=models.CASCADE)
    expertAssessment = models.ForeignKey(ExpertAssessment, on_delete=models.CASCADE)
    assessmentsControl = models.ForeignKey(AssessmentsControl,
                                           on_delete=models.CASCADE,
                                           null=True,
                                           related_name='actionImplementation'
                                           )
    services = models.ManyToManyField(Services, related_name='actionImplementation')
    expert = models.ManyToManyField(Expert,related_name='actionImplementation')
    expertise = models.ManyToManyField(Expertise, related_name='actionImplementation')

    class Meta:
        ordering = ['id']
