from django.db import models
from .messages_usp import OptionsUsp

# Begin Multidisciplinary Domain
class FallsUsp (models.Model):
    q88_falls_last_year = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q88_amount_falls_last_year = models.IntegerField(default=0)
    q89_fractures_due_to_falls = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q89_fractures_due_to_falls_list = models.TextField(null=True)
    q90_falls_activity = models.TextField(null=True)
    q91_strength_mmii = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q92_equilibrium = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q93_walking_aid_device = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)

    q94_older_than75 = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q95_female = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q96_cognitive_alterations = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q97_av_ds_commitment = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q98_visual_deficit = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q99_domestic_risks = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q100_behavior_risk = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q101_inactivity = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q102_prior_ave = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q103_psychotropic_medications_use = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q104_has_diseases = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
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
    comments = models.TextField('Observações Sobre o Bloco Multidimensional', blank=True, null=True)
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
