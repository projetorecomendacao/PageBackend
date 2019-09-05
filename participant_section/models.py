from django.db import models
from institution_section.models import Address


class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    profile_photo_URL = models.ImageField(upload_to='profile_photos', null=True)
    communication = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    weight = models.FloatField()
    height = models.FloatField()

    class Meta:
        ordering = ['id']

    def BMI(self):
        pass


class Income (models.Model):
    # range

    class Meta:
        ordering = ['id']


class ParticipantSocialMedia (models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


class MaritalStatus (models.Model):
    status = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']


class Schooling(models.Model):
    schooling = models.CharField(max_length=25)

    class Meta:
        ordering = ['id']


class ProfessionalsActivities(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Religion(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class ParticipantSituation (models.Model):
    date = models.DateField()
    study_time = models.IntegerField()

#    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='participant_situation')
    current_situation = models.OneToOneField(Participant, on_delete=models.DO_NOTHING, related_name='current_situation')
    history = models.ForeignKey(Participant, on_delete=models.DO_NOTHING, related_name='situation_history', blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='participant_situations')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.DO_NOTHING,
                                       related_name='participant_situations', blank=True)
    schooling = models.ForeignKey(Schooling, on_delete=models.DO_NOTHING, related_name='participant_situations',
                                  blank=True)
    work_professionals_activities = models.ManyToManyField(ProfessionalsActivities,
                                                           related_name='work_participant_situations', blank=True)
    retire_professionals_activities = models.ManyToManyField(ProfessionalsActivities,
                                                             related_name='retire_participant_situations', blank=True)
    religion = models.ForeignKey(Religion, on_delete=models.DO_NOTHING, related_name='participant_situations')
    income = models.ForeignKey(Income, on_delete=models.DO_NOTHING, related_name='participant_situations')
    lives_with = models.ManyToManyField(ParticipantSocialMedia, related_name='lives_with')
    rides_with = models.ManyToManyField(ParticipantSocialMedia, related_name='rides_with')

    class Meta:
        ordering = ['id']
