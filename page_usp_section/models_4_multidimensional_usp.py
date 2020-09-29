from django.db import models
from .messages_usp import OptionsUsp

# Begin Multidisciplinary Domain
class FallsUsp (models.Model):
    q88_falls_last_year = models.CharField(OptionsUsp.questions[87][0], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q88_amount_falls_last_year = models.IntegerField(OptionsUsp.questions[87][1],default=0)
    q89_fractures_due_to_falls = models.CharField(OptionsUsp.questions[88][0], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q89_fractures_due_to_falls_list = models.TextField(OptionsUsp.questions[88][1])
    q90_falls_activity = models.TextField(OptionsUsp.questions[90], null=True)
    q91_strength_mmii = models.CharField(OptionsUsp.questions[90], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q92_equilibrium = models.CharField(OptionsUsp.questions[91], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q93_walking_aid_device = models.CharField(OptionsUsp.questions[91], max_length=1, default="N", choices=OptionsUsp.CHOICES)

    q94_older_than75 = models.CharField(OptionsUsp.questions[92], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q95_female = models.CharField(OptionsUsp.questions[93], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q96_cognitive_alterations = models.CharField(OptionsUsp.questions[94], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q97_av_ds_commitment = models.CharField(OptionsUsp.questions[95], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q98_visual_deficit = models.CharField(OptionsUsp.questions[96], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q99_domestic_risks = models.CharField(OptionsUsp.questions[97], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q100_behavior_risk = models.CharField(OptionsUsp.questions[98], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q101_inactivity = models.CharField(OptionsUsp.questions[99], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q102_prior_ave = models.CharField(OptionsUsp.questions[100], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q103_psychotropic_medications_use = models.CharField(OptionsUsp.questions[101], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q104_has_diseases = models.CharField(OptionsUsp.questions[102], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Quedas'
        verbose_name_plural = 'Quedas'

    def score(self):
        pass


class MultidisciplinaryDomainUsp (models.Model):
    falls = models.OneToOneField(FallsUsp, on_delete=models.CASCADE, null=True)
    comments = models.TextField('Observações Sobre o Bloco Multidimensional')
    maxScore = models.IntegerField('Pontuação Máxima',default=8)

    def investigate(self):
        pass

    def score(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        #for score in (self.falls,):
        #    max_score += score.maxScore
        self.maxScore = max_score

    class Meta:
        ordering = ['id']
        verbose_name = 'Domínio Multidimensional'
        verbose_name_plural = 'Domínio Multidimensional'
# End Multidisciplinary Domain
