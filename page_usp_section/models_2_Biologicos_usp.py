from django.db import models
from .messages_usp import OptionsUsp
from health_section.models import Medicines

# Begin Biological Aspects
class SensoryDeficitUsp(models.Model):
    q20_vision_problems = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q21_hearing_problems = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q22_taste_problems = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q23_do_activities_problems = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Sensorial'
        verbose_name_plural = 'Déficit Sensorial'


class FunctionalDisabilityUsp (models.Model):
    q24_to_shop = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q25_use_transport = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q26_to_cook = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q27_useTelephone = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q28_dress_up = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q29_takeShower = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Incapacidade Funcional'
        verbose_name_plural = 'Incapacidade Funcional'


class MalnutritionUsp (models.Model):
    d30_difficulty_chewing = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    d31_less3_meal_daily = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    d32_decreases_amount_food = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    d33_lost_weight_no_reason = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    d33_lost_weight_no_reason_amount = models.CharField(max_length=30, default="N")
    d34_stress_illness_hospitalization = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q35_bmi_less22 = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)  # Usar cálculo de BMI do participante
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Desnutrição'
        verbose_name_plural = 'Desnutrição'


class CardiovascularFactorsUsp (models.Model):
    q36_dcv_familiar_history = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q37_hypertension = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q38_uncontrolled_diabetes = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q39_cholesterol = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q37_hypertension_unknow = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES, null=True, blank=True)
    q38_uncontrolled_diabetes_unknow = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES, null=True, blank=True)
    q39_cholesterol_unknow = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES, null=True, blank=True)
    q40_smoker = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q41_drink_type = models.CharField(max_length=50)
    q41_alcohol_Ingested_last_week_amount = models.TextField(null=True,blank=True)
    q41_alcohol_Ingested_last_week =  models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q42_practice_exercises_regularly = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q42_practise_exercises_frequency = models.CharField(max_length=50)
    q42_practise_exercises_time = models.CharField(max_length=50)
    q42_practice_exercises = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q43_bmi_obesity = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)  # Usar cálculo do BMI de participante
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Doenças Cardiovasculares (DCV)'
        verbose_name_plural = 'Doenças Cardiovasculares (DCV)'


class MisuseMedicationsUsp (models.Model):
    q44_diseases_last_5_years_a = models.CharField(OptionsUsp.questions[42][1], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_b = models.CharField(OptionsUsp.questions[42][2], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_c = models.CharField(OptionsUsp.questions[42][3], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_d = models.CharField(OptionsUsp.questions[42][4], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_e = models.CharField(OptionsUsp.questions[42][5], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_f = models.CharField(OptionsUsp.questions[42][6], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_g = models.CharField(OptionsUsp.questions[42][7], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_h = models.CharField(OptionsUsp.questions[42][8], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_i = models.CharField(OptionsUsp.questions[42][9], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_j = models.CharField(OptionsUsp.questions[42][10], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_k = models.CharField(OptionsUsp.questions[42][11], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_l = models.CharField(OptionsUsp.questions[42][12], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q44_diseases_last_5_years_l_other = models.CharField(OptionsUsp.questions[42][12], max_length=200, blank=True, null=True)
    q44_diseases_last_5_years_amount = models.IntegerField(OptionsUsp.questions[42][12],default=0)

    q45_health_problems_a = models.CharField(OptionsUsp.questions[43][1], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_b = models.CharField(OptionsUsp.questions[43][2], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_c = models.CharField(OptionsUsp.questions[43][3], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_d = models.CharField(OptionsUsp.questions[43][4], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_e = models.CharField(OptionsUsp.questions[43][5], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_f = models.CharField(OptionsUsp.questions[43][6], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_g = models.CharField(OptionsUsp.questions[43][7], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_h = models.CharField(OptionsUsp.questions[43][8], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q45_health_problems_h_other = models.CharField(OptionsUsp.questions[43][8], max_length=30, blank=True, null=True)


#    q46_medicines = models.ManyToManyField(Medicines, verbose_name="Medicamentos")
    q46_medicines = models.TextField("Medicamentos",null=True)
    q46_medicines_polypharmacy = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q47_know_medicines = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q48_medicines_increase = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q49_medicine_medical_precribed = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q50_medicine_medical_advice = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q51_already_stopped_medicines = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q52_self_medication = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q53_inappropriate_medication = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q54_risk_adverse_reaction = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Uso Inadequado de Medicamentos'
        verbose_name_plural = 'Uso Inadequado de Medicamentos'


class BiologicalAspectsUsp (models.Model):
    sensoryDeficit = models.OneToOneField(SensoryDeficitUsp, on_delete= models.CASCADE)
    functionalDisability = models.OneToOneField(FunctionalDisabilityUsp, on_delete=models.CASCADE)
    malNutrition = models.OneToOneField(MalnutritionUsp, on_delete=models.CASCADE)
    cardiovascularFactors = models.OneToOneField(CardiovascularFactorsUsp, on_delete=models.CASCADE)
    misuseMedications = models.OneToOneField(MisuseMedicationsUsp, on_delete= models.CASCADE)
    comments = models.TextField('Observações Sobre o Bloco Biológico', blank=True, null=True)
    max_score = models.IntegerField('Pontuação Máxima',default=36)
    score = models.IntegerField(null=True)

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


# End Biological Aspects
