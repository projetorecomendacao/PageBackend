from django.db import models
from .messages import Options
# Begin psychological aspects
class CognitionDeficit (models.Model):
    q1_memory_good_like_before = models.CharField(Options.questions[1],max_length=1,default="N",choices=Options.CHOICES)
    q2_memory_test = models.CharField(Options.questions[2][0],max_length=1,default="N",choices=Options.CHOICES)
    q2_memory_test_score = models.IntegerField(Options.questions[2][1], null=True, blank=True)
    q3_language_function_attention = models.CharField(Options.questions[3][0], max_length=1, default="N", choices=Options.CHOICES)
    q3_language_function_attention_score = models.IntegerField(Options.questions[3][1], default=0)
    q3_language_function_attention_15 = models.TextField(null=True)
    q3_language_function_attention_30 = models.TextField(null=True)
    q3_language_function_attention_45 = models.TextField(null=True)
    q3_language_function_attention_60 = models.TextField(null=True)
    q4_visospatial_ability = models.CharField(Options.questions[4][0], max_length=1, default="N", choices=Options.CHOICES)
    q4_visospatial_ability_score = models.IntegerField(Options.questions[4][1], default=0)
    q5_praxia = models.CharField(Options.questions[5][0], max_length=1,default="N",choices=Options.CHOICES)
    q5_praxia_score = models.IntegerField(Options.questions[5][1], default=0)
    q6_memory_test = models.CharField(Options.questions[6][0], max_length=1,default="N",choices=Options.CHOICES)
    q6_memory_test_score = models.IntegerField(Options.questions[6][1], default=0)
    need_investigation_cognition = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_cognition = models.IntegerField(default=6)
    score = models.IntegerField(null=True,default=0)


    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Cognitivo'
        verbose_name_plural = 'Déficit Cognitivo'


class AgingAspects (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']
        verbose_name = 'Aspectos relativos ao envelhecimento'
        verbose_name_plural = 'Aspectos relativos ao envelhecimento'

class NegativeAttitudesAging (models.Model):
    q7_age_self_perception = models.IntegerField(Options.questions[7][0], blank=True, null=True)
    q7_age_self_perception_why = models.TextField(Options.questions[7][1], blank=True, null=True)
    q7_age_self_perception_analyze = models.CharField(Options.questions[7][2], max_length=1, default="N", choices=Options.CHOICES)
    q8_aging_positive_points = models.TextField(Options.questions[8][1], blank=True, null=True)
    q8_aging_negative_points = models.TextField(Options.questions[8][2], blank=True, null=True)
    q8_aging_analyse = models.CharField(Options.questions[8][0], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_negative = models.CharField(Options.need_investigation_question, max_length=1,default="N",choices=Options.CHOICES)
    max_score_negative = models.IntegerField(default=2)
    score = models.IntegerField (null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Atitudes Negativas em Relação ao Processo de Envelhecimento'
        verbose_name_plural = 'Atitudes Negativas em Relação ao Processo de Envelhecimento'


class Depression (models.Model):
    q9_satisfied_with_life = models.CharField(Options.questions[9], max_length=1,default="N",choices=Options.CHOICES)
    q10_frequently_sad = models.CharField(Options.questions[10],max_length=1,default="N",choices=Options.CHOICES)
    q11_stopped_doing_things = models.CharField(Options.questions[11],max_length=1,default="N",choices=Options.CHOICES )
    q12_fear_bad_things_happen = models.CharField(Options.questions[12],max_length=1,default="N",choices=Options.CHOICES)
    q13_impatient_disquiet = models.CharField(Options.questions[13], max_length=1,default="N",choices=Options.CHOICES)
    q14_concentration_problem = models.CharField(Options.questions[14],max_length=1, default="N",choices=Options.CHOICES)
    need_investigation_depression = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_depression = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Depressão'
        verbose_name_plural = 'Depressão'

class PsychologicalAspects (models.Model):
    cognition_deficit = models.OneToOneField(CognitionDeficit, on_delete=models.CASCADE, null=True,verbose_name='Déficit Cognitivo')
    negative_attitudes_aging = models.OneToOneField(NegativeAttitudesAging, on_delete=models.CASCADE, null=True ,verbose_name='Atitude Negativa em Relação ao Envelhecimento')
    depression = models.OneToOneField(Depression,  on_delete=models.CASCADE, null=True,verbose_name='Depressão')
    comments_psico = models.TextField("Observações sobre o bloco Psicológico", null=True)
    max_score_psico = models.IntegerField('Pontuação Máxima',default=14)

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        for score in (self.cognition_deficit, self.negative_attitudes_aging, self.depression):
           pass
           # max_score += score.max_score
        self.max_score = max_score

    class Meta:
        ordering = ['id']
        verbose_name= "Relacionados a Aspectos Psicológicos"
        verbose_name_plural= "Relacionados a Aspectos Psicológicos"

    def score(self):
        pass
# End psychological aspects
