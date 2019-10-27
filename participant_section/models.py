from django.db import models
from institution_section.models import Address
from page_section.messages import Options


class Participant(models.Model):
    p00_email = models.CharField("Email da Google", null=True, blank=True, max_length=80)
    p01_name = models.CharField('Nome:', max_length=50)
    p02_address = models.CharField("Endereço", max_length=80 )
    p03_communication = models.CharField('Meios de Entrar em contato', max_length=100)
    p04_birth_date = models.DateField('Data de Nascimento')
    p05_age = models.IntegerField('Idade Atual')
    p06_gender = models.CharField('Gênero:', max_length=1, )
    p20_profile_photo_URL = models.ImageField(upload_to='profile_photos', null=True)


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
#    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='participant_situation')
#    current_situation = models.OneToOneField(Participant, on_delete=models.DO_NOTHING, related_name='current_situation')
#    history = models.ForeignKey(Participant, on_delete=models.DO_NOTHING, related_name='situation_history', blank=True)
#    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='participant_situations')
    p07_marital_status = models.CharField('Estado Civil', max_length=30, choices=Options.MARITALSTATUS)
    p08_schooling = models.CharField('Escolaridade', max_length=35, choices=Options.SCHOOL)
    p09_study_time = models.IntegerField('Tempo de Estudo', null=True, blank=True)
    p10_is_retired = models.CharField("É Aposentado ou pensionista?", max_length=1,choices=Options.CHOICES)
    p10_retired_profession = models.CharField('Aposentado por qual profissao', max_length=30, null=True, blank=True)
    p10_actual_profession = models.CharField('Profissão Atual', max_length=30, null=True, blank=True)
    p11_retire_more_time_activity = models.CharField('Se aposentado, qual profissão exerceu por mais tempo', max_length=30, null=True, blank='True')
    p12_is_working_professionals_activities = models.CharField("Exerce atividade remunerada?", max_length=1, choices=Options.CHOICES)
    p12_professional_activities = models.CharField('Atividade Remunerada exercida:', max_length=30, null=True, blank=True)
    p13_income_I = models.CharField('Rendimento Mensal Individual:', max_length=70, choices=Options.INCOME)
    p13_income_F = models.CharField('Rendimento Mensal Familiar:', max_length=70, choices=Options.INCOME)
    p14_lives_with = models.TextField("Com quem mora", null=True, blank=True)
    p15_has_religion = models.CharField("Possui Religião", max_length=1, choices=Options.CHOICES)
    p15_religion = models.CharField('Religião', max_length=30, null=True, blank=True)
    p16_health_self_report = models.TextField("Auto Relato de Saúde", null=True, blank=True)
    p20_weight = models.FloatField("Peso", null=True, blank=True)
    p20_height = models.FloatField("Altura", null=True, blank=True)
    p20_IMC = models.FloatField("IMC", null=True, blank=True)
    p30_ride_with = models.TextField("Pessoas com a qual pega carona", null=True, blank=True)

    class Meta:
        ordering = ['id']
