from django.db import models
from institution_section.models import Location
from activities_section.models import Activity
from participant_section.models import Participant


class Offers(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField()
    schedules = models.CharField(max_length=50)
    cost = models.CharField(max_length=30)
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='offers', blank=True, null=True)
    activities = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, related_name='offers', blank=True, null=True)
    #participants = models.ManyToManyField(Participant, related_name='offers', blank=True)

    class Meta:
        ordering = ['id']


class Review(models.Model):
    rate = models.IntegerField()
    date = models.DateField()

    participant = models.ForeignKey(Participant, on_delete=models.DO_NOTHING, related_name='reviews')
    offer = models.ForeignKey(Offers, on_delete=models.DO_NOTHING, related_name='reviews')
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, related_name='reviews')

    class Meta:
        ordering = ['id']
