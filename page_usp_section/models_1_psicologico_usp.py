from django.db import models
from .messages_usp import OptionsUsp
# Begin psychological aspects
class CognitionDeficitUsp (models.Model):

    q1_memory_good_like_others = models.CharField(OptionsUsp.questions[1],max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q2_three_words = models.CharField(OptionsUsp.questions[2],max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q3_15 = models.CharField(OptionsUsp.questions[3][0],null=True,max_length=50)
    q3_30 = models.CharField(OptionsUsp.questions[3][1],null=True,max_length=50)
    q3_45 = models.CharField(OptionsUsp.questions[3][1],null=True,max_length=50)
    q3_60 = models.CharField(OptionsUsp.questions[3][1],null=True,max_length=50)
    q3_animals = models.CharField(OptionsUsp.questions[3][1],max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q4_three_words= models.CharField(OptionsUsp.questions[4], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q5_three_commands = models.CharField(OptionsUsp.questions[5], max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q6_clock = models.CharField(OptionsUsp.questions[6], max_length=1,default="N",choices=OptionsUsp.CHOICES)
    cognition_deficit_obs = models.TextField("Observações",null=True)
    need_investigation_cognition = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score_cognition = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Cognitivo'
        verbose_name_plural = 'Déficit Cognitivo'


class NegativeAttitudesAgingUsp (models.Model):
 
    q7_age_self_perception = models.IntegerField(OptionsUsp.questions[7][0], blank=True, null=True, default=0)
    q7_age_self_perception_why = models.TextField(OptionsUsp.questions[7][1], blank=True, null=True)
    q7_age_self_perception_analyze = models.CharField(OptionsUsp.questions[7][2], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q8_good_health = models.CharField(OptionsUsp.questions[8], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q9_more_neg_pos = models.CharField(OptionsUsp.questions[9], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q10_worried = models.CharField(OptionsUsp.questions[10], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q11_sex_life = models.CharField(OptionsUsp.questions[11], max_length=1, default="N", choices=OptionsUsp.CHOICES) 
    q12_little_to_do = models.CharField(OptionsUsp.questions[12], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q13_physical_weakness = models.CharField(OptionsUsp.questions[13], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q14_better_die = models.CharField(OptionsUsp.questions[14], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    negative_obs = models.TextField("Observações", null=True)
    need_investigation_negative = models.CharField(OptionsUsp.need_investigation_question, max_length=1,default="N",choices=OptionsUsp.CHOICES)
    max_score_negative = models.IntegerField(default=2)
    score = models.IntegerField(null=True)


    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Atitudes Negativas em Relação ao Processo de Envelhecimento'
        verbose_name_plural = 'Atitudes Negativas em Relação ao Processo de Envelhecimento'


class DepressionUsp (models.Model):
    q15_satisfied_with_life = models.CharField(OptionsUsp.questions[15], max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q16_frequently_sad = models.CharField(OptionsUsp.questions[16],max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q17_stopped_doing_things = models.CharField(OptionsUsp.questions[17],max_length=1,default="N",choices=OptionsUsp.CHOICES )
    q18_fear_bad_things_happen = models.CharField(OptionsUsp.questions[18],max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q19_impatient_disquiet = models.CharField(OptionsUsp.questions[19], max_length=1,default="N",choices=OptionsUsp.CHOICES)
    depression_obs = models.TextField("Observações", null = True)
    need_investigation_depression = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score_depression = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Depressão'
        verbose_name_plural = 'Depressão'


class PsychologicalAspectsUsp (models.Model):
    cognition_deficit = models.OneToOneField(CognitionDeficitUsp, on_delete=models.CASCADE, null=True,verbose_name='Déficit Cognitivo')
    negative_attitudes_aging = models.OneToOneField(NegativeAttitudesAgingUsp, on_delete=models.CASCADE, null=True ,verbose_name='Atitude Negativa em Relação ao Envelhecimento')
    depression = models.OneToOneField(DepressionUsp,  on_delete=models.CASCADE, null=True,verbose_name='Depressão')
    comments_psico = models.TextField("Observações sobre o bloco Psicológico")
    max_score_psico = models.IntegerField('Pontuação Máxima',default=14)
    

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    class Meta:
        ordering = ['id']
        verbose_name= "Relacionados a Aspectos Psicológicos"
        verbose_name_plural= "Relacionados a Aspectos Psicológicos"

    def score(self):
        pass
# End psychological aspects
