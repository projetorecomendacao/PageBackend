from django.db import models
from .messages import Options

# Begin Multidisciplinary Domain
class Falls (models.Model):
    q87_falls_last_year = models.CharField(Options.questions[87][0], max_length=1, default="N", choices=Options.CHOICES)
    q87_amount_falls_last_year = models.IntegerField(Options.questions[87][1])
    q88_fractures_due_to_falls = models.CharField(Options.questions[88][0], max_length=1, default="N", choices=Options.CHOICES)
    q88_fractures_due_to_falls_list = models.TextField(Options.questions[88][1])
    q89_fractures_list = models.TextField(Options.questions[89], null=True, blank=True)
    q90_strength_mmii = models.CharField(Options.questions[90], max_length=1, default="N", choices=Options.CHOICES)
    q91_equilibrium = models.CharField(Options.questions[91], max_length=1, default="N", choices=Options.CHOICES)
    q92_older_than75 = models.CharField(Options.questions[92], max_length=1, default="N", choices=Options.CHOICES)
    q93_female = models.CharField(Options.questions[93], max_length=1, default="N", choices=Options.CHOICES)
    q94_cognitive_alterations = models.CharField(Options.questions[94], max_length=1, default="N", choices=Options.CHOICES)
    q95_av_ds_commitment = models.CharField(Options.questions[95], max_length=1, default="N", choices=Options.CHOICES)
    q96_visual_deficit = models.CharField(Options.questions[96], max_length=1, default="N", choices=Options.CHOICES)
    q97_domestic_risks = models.CharField(Options.questions[97], max_length=1, default="N", choices=Options.CHOICES)
    q98_behavior_risk = models.CharField(Options.questions[98], max_length=1, default="N", choices=Options.CHOICES)
    q99_inactivity = models.CharField(Options.questions[99], max_length=1, default="N", choices=Options.CHOICES)
    q100_prior_ave = models.CharField(Options.questions[100], max_length=1, default="N", choices=Options.CHOICES)
    q101_psychotropic_medications_use = models.CharField(Options.questions[101], max_length=1, default="N", choices=Options.CHOICES)
    q102_has_diseases = models.CharField(Options.questions[102], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_falls = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    score = models.IntegerField(null=True)
    max_score_falls = models.IntegerField(default=16)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Quedas'
        verbose_name_plural = 'Quedas'


class MultidisciplinaryDomain (models.Model):
    falls = models.OneToOneField(Falls, on_delete=models.CASCADE, null=True)
    comments_multi = models.TextField('Observações Sobre o Bloco Multidimensional')
    maxScore_multi = models.IntegerField('Pontuação Máxima',default=8)

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
