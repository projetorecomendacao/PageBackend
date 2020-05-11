from django.db import models
from .messages import Options
# Begin Biological Aspects
class SensoryDeficit(models.Model):
    q15_vision_problems = models.CharField(Options.questions[15],  max_length=1, default="N", choices=Options.CHOICES)
    q16_hearing_problems = models.CharField(Options.questions[16],  max_length=1, default="N", choices=Options.CHOICES)
    q17_taste_problems = models.CharField(Options.questions[17],  max_length=1, default="N", choices=Options.CHOICES)
    q18_senses_problems = models.CharField(Options.questions[18], max_length=1, default="N", choices=Options.CHOICES)
    q19_interaction_problems = models.CharField(Options.questions[19], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_sensory = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    score: models.IntegerField(null=True)
    max_score_sensory = models.IntegerField(default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Sensorial'
        verbose_name_plural = 'Déficit Sensorial'




class FunctionalDisability (models.Model):
    q20_to_shop = models.CharField(Options.questions[20],  max_length=1, default="N", choices=Options.CHOICES)
    q21_use_transport = models.CharField(Options.questions[21],  max_length=1, default="N", choices=Options.CHOICES)
    q22_to_cook = models.CharField(Options.questions[22],  max_length=1, default="N", choices=Options.CHOICES)
    q23UseTelephone = models.CharField(Options.questions[23],  max_length=1, default="N", choices=Options.CHOICES)
    q24_dress_up = models.CharField(Options.questions[24],  max_length=1, default="N", choices=Options.CHOICES)
    q25TakeShower = models.CharField(Options.questions[25],  max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_functional = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_functional = models.IntegerField('Pontuação Máxima',default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Incapacidade Funcional'
        verbose_name_plural = 'Incapacidade Funcional'

    def score(self):
        pass


class Malnutrition (models.Model):
    q26_yourself_malnourished = models.CharField(Options.questions[26], max_length=1, default="N", choices=Options.CHOICES)
    q27_chewing_mouth_problems = models.CharField(Options.questions[27], max_length=1, default="N", choices=Options.CHOICES)
    q28_less3_meal_daily = models.CharField(Options.questions[28], max_length=1, default="N", choices=Options.CHOICES)
    q29_decreases_amount_food = models.CharField(Options.questions[29], max_length=1, default="N", choices=Options.CHOICES)
    q30_lost_weight_no_reason = models.CharField(Options.questions[30], max_length=15, default="N", choices=Options.LOSTWEIGHT)
    q30_lost_weight_no_reason_amount = models.CharField(max_length=20, null=True)    
    q31_stress_illness_hospitalization = models.CharField(Options.questions[31], max_length=1, default="N", choices=Options.CHOICES)
    q31_stress = models.CharField(max_length=1, default="N", choices=Options.CHOICES)
    q31_illnes = models.CharField(max_length=1, default="N", choices=Options.CHOICES)
    q31_hospital = models.CharField(max_length=1, default="N", choices=Options.CHOICES)
    q32_bmi_less22 = models.CharField(Options.questions[32], max_length=1, default="N", choices=Options.CHOICES)  # Usar cálculo de BMI do participante
    score: models.IntegerField(null=True)
    need_investigation_malnutrition = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_malnutrition = models.IntegerField('Pontuação Máxima',default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Desnutrição'
        verbose_name_plural = 'Desnutrição'


class CardiovascularFactors (models.Model):
    q33_dcv_familiar_history = models.CharField(Options.questions[33], max_length=1, default="N", choices=Options.CHOICES)
    q34_hypertension = models.CharField(Options.questions[34][0], max_length=1, default="N", choices=Options.CHOICES)
    q34_hypertension_unknow = models.CharField(Options.questions[34][1], max_length=1, default="N", choices=Options.CHOICES)
    q35_uncontrolled_diabetes = models.CharField(Options.questions[35][0], max_length=1, default="N", choices=Options.CHOICES)
    q35_unknown_value_glycemia = models.CharField(Options.questions[35][1], max_length=1, default="N", choices=Options.CHOICES)
    q36_cholesterol = models.CharField(Options.questions[36][0], max_length=1, default="N", choices=Options.CHOICES)
    q36_unknown_value_ct_hdl = models.CharField(Options.questions[36][1], max_length=1, default="N", choices=Options.CHOICES)
    q37_smoker = models.CharField(Options.questions[37], max_length=1, default="N", choices=Options.CHOICES)
    q38_practice_150_minutes_exercises = models.CharField(Options.questions[38], max_length=1, default="N", choices=Options.CHOICES)
    q39_healthy_eating = models.CharField(Options.questions[39], max_length=1, default="N", choices=Options.CHOICES)
    q40_alcohol_Ingested_last_week =  models.CharField(Options.questions[40][0], max_length=1, default="N", choices=Options.CHOICES)
    q40_alcohol_Ingested_last_week_amount = models.TextField(Options.questions[40][1],null=True,blank=True)
    q41_bmi_obesity = models.CharField(Options.questions[41], max_length=1, default="N", choices=Options.CHOICES)  # Usar cálculo do BMI de participante
    need_investigation_cardio = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    score: models.IntegerField(null=True)
    max_score_cardio = models.IntegerField('Pontuação Máxima',default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Doenças Cardiovasculares (DCV)'
        verbose_name_plural = 'Doenças Cardiovasculares (DCV)'




class MisuseMedications (models.Model):
    q42_diseases_last_5_years_a = models.CharField(Options.questions[42][1], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_b = models.CharField(Options.questions[42][2], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_c = models.CharField(Options.questions[42][3], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_d = models.CharField(Options.questions[42][4], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_e = models.CharField(Options.questions[42][5], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_f = models.CharField(Options.questions[42][6], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_g = models.CharField(Options.questions[42][7], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_h = models.CharField(Options.questions[42][8], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_i = models.CharField(Options.questions[42][9], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_j = models.CharField(Options.questions[42][10], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_k = models.CharField(Options.questions[42][11], max_length=1, default="N", choices=Options.CHOICES)
    q42_diseases_last_5_years_l = models.CharField(Options.questions[42][12], max_length=30, blank=True, null=True)

    q43_health_problems_a = models.CharField(Options.questions[43][1], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_b = models.CharField(Options.questions[43][2], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_c = models.CharField(Options.questions[43][3], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_d = models.CharField(Options.questions[43][4], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_e = models.CharField(Options.questions[43][5], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_f = models.CharField(Options.questions[43][6], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_g = models.CharField(Options.questions[43][7], max_length=1, default="N", choices=Options.CHOICES)
    q43_health_problems_h = models.CharField(Options.questions[43][8], max_length=30, blank=True, null=True)

    q44_amount_diagnostics = models.IntegerField(Options.questions[44])
    q45_medicines = models.TextField(Options.questions[45], null=True, blank=True)
    q46_medicines_increase = models.CharField(Options.questions[46], max_length=1, default="N", choices=Options.CHOICES)
    q47_know_medicines = models.CharField(Options.questions[47], max_length=1, default="N", choices=Options.CHOICES)
    q48_medications_prescribed = models.CharField(Options.questions[48], max_length=1, default="N", choices=Options.CHOICES)
    q49_medicine_medical_advice = models.CharField(Options.questions[49], max_length=1, default="N", choices=Options.CHOICES)
    q50_already_stopped_medicines = models.CharField(Options.questions[50], max_length=1, default="N", choices=Options.CHOICES)
    q51_self_medication = models.CharField(Options.questions[51], max_length=1, default="N", choices=Options.CHOICES)
    q52_inappropriate_medication = models.CharField(Options.questions[52], max_length=1, default="N", choices=Options.CHOICES)
    q53_risk_adverse_reaction = models.CharField(Options.questions[53], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_misuse = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_misuse = models.IntegerField('Pontuação Máxima',default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Uso Inadequado de Medicamentos'
        verbose_name_plural = 'Uso Inadequado de Medicamentos'

    def score(self):
        pass


class BiologicalAspects (models.Model):
    sensoryDeficit = models.OneToOneField(SensoryDeficit, on_delete= models.CASCADE)
    functionalDisability = models.OneToOneField(FunctionalDisability, on_delete=models.CASCADE)
    malNutrition = models.OneToOneField(Malnutrition, on_delete=models.CASCADE)
    cardiovascularFactors = models.OneToOneField(CardiovascularFactors, on_delete=models.CASCADE)
    misuseMedications = models.OneToOneField(MisuseMedications, on_delete= models.CASCADE)
    comments_bio = models.TextField('Observações Sobre o Bloco Biológico')
    max_score_bio = models.IntegerField('Pontuação Máxima',default=36)

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        #for score in (self.sensoryDeficit, self.functionalDisability, self.malNutrition,
        #              self.cardiovascularFactors, self.misuseMedications):
        #    max_score += score.maxScore
        self.max_score = max_score

    class Meta:
        ordering = ['id']
        verbose_name = 'Relacionados a Aspectos Biológicos'
        verbose_name_plural = 'Relacionados a Aspectos Biológicos'

    def score(self):
        pass
# End Biological Aspects
