from django.db import models
from .messages_usp import OptionsUsp
# Begin psychological aspects
class CognitionDeficitUsp (models.Model):

    q1_memory_good_like_others = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q2_three_words = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q3_15 = models.TextField(null=True,blank=True)
    q3_30 = models.TextField(null=True,blank=True)
    q3_45 = models.TextField(null=True,blank=True)
    q3_60 = models.TextField(null=True,blank=True)
    q3_animals = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q4_three_words= models.CharField( max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q5_three_commands = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q6_clock = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Cognitivo'
        verbose_name_plural = 'Déficit Cognitivo'


class NegativeAttitudesAgingUsp (models.Model):
 
    q7_age_self_perception = models.IntegerField(blank=True, null=True, default=0)
    q7_age_self_perception_why = models.TextField(blank=True, null=True)
    q7_age_self_perception_analyze = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q8_good_health = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q9_more_neg_pos = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q10_worried = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q11_sex_life = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES) 
    q12_little_to_do = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q13_physical_weakness = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q14_better_die = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)


    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Atitudes Negativas em Relação ao Processo de Envelhecimento'
        verbose_name_plural = 'Atitudes Negativas em Relação ao Processo de Envelhecimento'


class DepressionUsp (models.Model):
    q15_satisfied_with_life = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q16_frequently_sad = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q17_stopped_doing_things = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES )
    q18_fear_bad_things_happen = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    q19_impatient_disquiet = models.CharField(max_length=1,default="N",choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
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
    comments = models.TextField("Observações sobre o bloco Psicológico", blank=True, null=True)
    max_score = models.IntegerField('Pontuação Máxima',default=14)
    

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
