from django.db import models
from activities_section.models import Activity
from institution_section.models import Location, Institution


class Offers(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField()
    schedules = models.CharField(max_length=50)
    cost = models.CharField(max_length=30)
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING, related_name='offers1', blank=True, null=True)
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='offers2', blank=True, null=True)
    activities = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, related_name='offers3', blank=True, null=True)

    class Meta:
        ordering = ['id']


class RecommendedActivitiesOffers(models.Model):
    data = models.DateField()
    offer = models.ForeignKey(Offers, on_delete=models.DO_NOTHING, related_name='offers4', blank=True, null=True, verbose_name="Atividade Ofertada")
    systemRating = models.IntegerField()
    expertRating = models.IntegerField()
    accepted = models.BooleanField()
    expertConsideration = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Atividades Ofertadas Recomendadas'
        verbose_name_plural = 'Atividades Ofertadas Recomendadas'


class RecommendedActivities(models.Model):
    data = models.DateField()
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, related_name='offers5', blank=True, null=True, verbose_name="Atividades")
    systemRating = models.IntegerField()
    expertRating = models.IntegerField()
    accepted = models.BooleanField()
    expertConsideration = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Atividades Recomendadas'
        verbose_name_plural = 'Atividades Recomendadas'