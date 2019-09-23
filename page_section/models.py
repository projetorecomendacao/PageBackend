from django.db import models

from health_section.models import Diseases, Medicines, HealthProblems, Fractures
from review_section.models import Offers
from drinks_section.models import IngestedDrinks
from assessment_section.models import ExpertAssessment
from experts_section.models import Gerontologist
from .messages import *

# Begin psychological aspects
class CognitionDeficit (models.Model):
    q1_memory_good_like_before = models.CharField(Options.questions[1],max_length=1,default="N",choices=Options.CHOICES)
    q2_memory_test = models.CharField(Options.questions[2],max_length=1,default="N",choices=Options.CHOICES)
    q3_language_function_attention = models.CharField(Options.questions[3], max_length=1, default="N", choices=Options.CHOICES)
    q4_visospatial_ability = models.CharField(Options.questions[4][0], max_length=1, default="N", choices=Options.CHOICES)
    q4_visospatial_ability_score = models.IntegerField(Options.questions[4][1], default=0)
    q5_praxia = models.CharField(Options.questions[5], max_length=1,default="N",choices=Options.CHOICES)
    q6_memory_test = models.CharField(Options.questions[6], max_length=1,default="N",choices=Options.CHOICES)
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=6)


    def score(self):
        pass

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Cognitivo'
        verbose_name_plural = 'Déficit Cognitivo'


class AgingAspects (models.Model):
    description: models.CharField(max_length=60)

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
    need_investigation = models.CharField(Options.need_investigation_question, max_length=1,default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=2)

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
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=6)

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
    comments = models.TextField("Observações sobre o bloco Psicológico")
    max_score = models.IntegerField('Pontuação Máxima',default=14)

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


# Begin Biological Aspects
class SensoryDeficit(models.Model):
    q15_vision_problems = models.CharField(Options.questions[15],  max_length=1, default="N", choices=Options.CHOICES)
    q16_hearing_problems = models.CharField(Options.questions[16],  max_length=1, default="N", choices=Options.CHOICES)
    q17_taste_problems = models.CharField(Options.questions[17],  max_length=1, default="N", choices=Options.CHOICES)
    q18_senses_problems = models.CharField(Options.questions[18], max_length=1, default="N", choices=Options.CHOICES)
    q19_interaction_problems = models.CharField(Options.questions[19], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Déficit Sensorial'
        verbose_name_plural = 'Déficit Sensorial'

    def score(self):
        pass


class FunctionalDisability (models.Model):
    q20_to_shop = models.CharField(Options.questions[20],  max_length=1, default="N", choices=Options.CHOICES)
    q21_use_transport = models.CharField(Options.questions[21],  max_length=1, default="N", choices=Options.CHOICES)
    q22_to_cook = models.CharField(Options.questions[22],  max_length=1, default="N", choices=Options.CHOICES)
    q23UseTelephone = models.CharField(Options.questions[23],  max_length=1, default="N", choices=Options.CHOICES)
    q24_dress_up = models.CharField(Options.questions[24],  max_length=1, default="N", choices=Options.CHOICES)
    q25TakeShower = models.CharField(Options.questions[25],  max_length=1, default="N", choices=Options.CHOICES)
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField('Pontuação Máxima',default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Incapacidade Funcional'
        verbose_name_plural = 'Incapacidade Funcional'

    def score(self):
        pass


class Malnutrition (models.Model):
    d26_yourself_malnourished = models.CharField(Options.questions[26], max_length=1, default="N", choices=Options.CHOICES)
    d27_chewing_mouth_problems = models.CharField(Options.questions[27], max_length=1, default="N", choices=Options.CHOICES)
    d28_less3_meal_daily = models.CharField(Options.questions[28], max_length=1, default="N", choices=Options.CHOICES)
    d29_decreases_amount_food = models.CharField(Options.questions[29], max_length=1, default="N", choices=Options.CHOICES)
    d30_lost_weight_no_reason = models.CharField(Options.questions[30], max_length=1, default="N", choices=Options.LOSTWEIGHT)
    d31_stress_illness_hospitalization = models.CharField(Options.questions[31], max_length=1, default="N", choices=Options.CHOICES)
    q32_bmi_less22 = models.CharField(Options.questions[32], max_length=1, default="N", choices=Options.CHOICES)  # Usar cálculo de BMI do participante
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField('Pontuação Máxima',default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Desnutrição'
        verbose_name_plural = 'Desnutrição'

    def score(self):
        pass


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
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField('Pontuação Máxima',default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Doenças Cardiovasculares (DCV)'
        verbose_name_plural = 'Doenças Cardiovasculares (DCV)'

    def score(self):
        pass


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
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField('Pontuação Máxima',default=9)

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
    comments = models.TextField('Observações Sobre o Bloco Biológico')
    max_score = models.IntegerField('Pontuação Máxima',default=36)

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


# Begin Social Aspects
class LowSocialSupport (models.Model):
    q54_spouse = models.CharField(Options.questions[54][0], max_length=1, default="N", choices=Options.CHOICES)
    q54_mother = models.CharField(Options.questions[54][1], max_length=1, default="N", choices=Options.CHOICES)
    q54_father = models.CharField(Options.questions[54][2], max_length=1, default="N", choices=Options.CHOICES)
    q54_brothers = models.IntegerField(Options.questions[54][3])
    q54_children = models.IntegerField(Options.questions[54][4],)
    q54_gran_children = models.IntegerField(Options.questions[54][5])
    q55_meet_family_friends = models.CharField(Options.questions[55], max_length=1, default="N", choices=Options.CHOICES)
    q56_participate_family_decisions = models.CharField(Options.questions[56], max_length=1, default="N", choices=Options.CHOICES)
    q57_satisfied_family_relationship = models.CharField(Options.questions[57], max_length=1, default="N", choices=Options.CHOICES)
    q58_helped_if_need_money = models.CharField(Options.questions[58], max_length=1, default="N", choices=Options.CHOICES)
    q59_someone_helps_if_need = models.CharField(Options.questions[59], max_length=1, default="N", choices=Options.CHOICES)
    q60_someone_to_have_fun = models.CharField(Options.questions[60], max_length=1, default="N", choices=Options.CHOICES)
    q61_participate_social_events = models.CharField(Options.questions[61], max_length=1, default="N", choices=Options.CHOICES)
    q62_regulary_healt_services = models.CharField(Options.questions[62], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Baixo Suporte Social'
        verbose_name_plural = 'Baixo Suporte Social'

    def score(self):
        pass


class EnvironmentalProblems (models.Model):
    # Internal environment
    q63_estable_furniture = models.CharField(Options.questions[63], max_length=1, default="N", choices=Options.CHOICES)
    q64_loose_objects_carpets = models.CharField(Options.questions[64], max_length=1, default="N", choices=Options.CHOICES)
    q65_slippery_floor = models.CharField(Options.questions[65], max_length=1, default="N", choices=Options.CHOICES)
    q66_handrail_on_stairs = models.CharField(Options.questions[66], max_length=1, default="N", choices=Options.CHOICES)
    q67_lighted_stairs = models.CharField(Options.questions[67], max_length=1, default="N", choices=Options.CHOICES)
    q68_suitable_stairs_steps = models.CharField(Options.questions[68], max_length=1, default="N", choices=Options.CHOICES)
    q69_non_slippery_carpet = models.CharField(Options.questions[69], max_length=1, default="N", choices=Options.CHOICES)

    # riskBehavior
    q70_get_on_stool = models.CharField(Options.questions[70], max_length=1, default="N", choices=Options.CHOICES)
    q71_turn_lights_off = models.CharField(Options.questions[71], max_length=1, default="N", choices=Options.CHOICES)
    q72_safe_shoes = models.CharField(Options.questions[72], max_length=1, default="N", choices=Options.CHOICES)

    # externalEnvironment
    q73_manicure_sidewalks = models.CharField(Options.questions[73], max_length=1, default="N", choices=Options.CHOICES)
    q74_public_transport_access = models.CharField(Options.questions[74], max_length=1, default="N", choices=Options.CHOICES)
    q75_commerce_access = models.CharField(Options.questions[75], max_length=1, default="N", choices=Options.CHOICES)
    q76_ease_plasewalking = models.CharField(Options.questions[76], max_length=1, default="N", choices=Options.CHOICES)
    q77_fun_access = models.CharField(Options.questions[77], max_length=1, default="N", choices=Options.CHOICES)
    q78_safety = models.CharField(Options.questions[78], max_length=1, default="N", choices=Options.CHOICES)

    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=16)

    def investigate(self):
        pass

    def score(self):
        pass

    def calcular(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Problemas Ambientais'
        verbose_name_plural = 'Problemas Ambientais'


class Violence (models.Model):
    q79_afraid_close_person = models.CharField(Options.questions[79], max_length=1, default="N", choices=Options.CHOICES)
    q80_feels_abandoned = models.CharField(Options.questions[80], max_length=1, default="N", choices=Options.CHOICES)
    q81_forced = models.CharField(Options.questions[81], max_length=1, default="N", choices=Options.CHOICES)
    q82_assauteld = models.CharField(Options.questions[82], max_length=1, default="N", choices=Options.CHOICES)
    q83_in_need = models.CharField(Options.questions[83], max_length=1, default="N", choices=Options.CHOICES)
    q84_someone_used_money = models.CharField(Options.questions[84], max_length=1, default="N", choices=Options.CHOICES)
    q85_touched_without_permission = models.CharField(Options.questions[85], max_length=1, default="N", choices=Options.CHOICES)
    q86_dont_take_care_health = models.CharField(Options.questions[86], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=8)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Violência'
        verbose_name_plural = 'Violência'

    def score(self):
        pass


class SocialAspects (models.Model):
    lowSocialSupport = models.OneToOneField(LowSocialSupport, on_delete=models.CASCADE, null=True)
    environmentalProblems = models.OneToOneField(EnvironmentalProblems, on_delete=models.CASCADE, null=True)
    violence = models.OneToOneField(Violence, on_delete=models.CASCADE, null=True)
    comments = models.TextField('Observações Sobre o Bloco Social')
    maxScore = models.IntegerField('Pontuação Máxima',default=32)

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        #for score in (self.lowSocialSupport, self.environmentalProblems, self.violence):
        #    max_score += score.maxScore
        self.maxScore = max_score

    class Meta:
        ordering = ['id']
        verbose_name = 'Relacionados a Aspectos Sociais'
        verbose_name_plural = 'Relacionados a Aspectos Sociais'

    def score(self):
        pass
# End Social Aspects


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
    need_investigation = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=8)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Quedas'
        verbose_name_plural = 'Quedas'

    def score(self):
        pass


class MultidisciplinaryDomain (models.Model):
    falls = models.OneToOneField(Falls, on_delete=models.CASCADE, null=True)
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


class DemandMap (models.Model):
    dm3_unmet_demands = models.TextField('O(a) idoso(a) apresenta outras demandas não contempladas no mapa? Se sim, especificar:',null=True)
    gerontologist_assessment =  models.TextField('Avaliação do Gerontólogo',null=True)

    def d1_domain_contribution_calculation(self):
        pass

    def d2_dimension_contribution_calculation(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Mapa das Demandas'
        verbose_name_plural = 'Mapa das Demandas'


class Page (models.Model):
    gerontologist = models.ForeignKey(Gerontologist, on_delete=models.CASCADE, null=True, verbose_name='Gerontologista Resposável')
    date = models.DateField("Data da Entrevista", null="True")
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null="True")
    p1_self_health_report = models.TextField("Auto Relato de Saúde - Como o senhor(a)", null=True)
    #Dimensões do Page
    psychologicalAspects = models.OneToOneField(PsychologicalAspects, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Psicológicos')
    biologicalAspects = models.OneToOneField(BiologicalAspects, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Biológicos')
    socialAspects = models.OneToOneField(SocialAspects, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Sociais')
    multidisciplinaryDomain = models.OneToOneField(MultidisciplinaryDomain, on_delete=models.CASCADE, null=True,verbose_name='Domínio Multidisciplinar')
    #Mapa de Demandas
    demandMap = models.OneToOneField(DemandMap,on_delete=models.CASCADE, null=True,verbose_name='Mapa de Demandas')
    #Avaliação Multidisciplinar
    expertAssessment = models.ForeignKey(ExpertAssessment, on_delete=models.CASCADE, null=True, verbose_name='Planejamento das Ações')
    #Atividades Recomendadas
    recommendedActivities = models.ManyToManyField(Offers,
                                                   through='RecommendedActivities',
                                                   related_name='page',
                                                   blank=True
                                                   )

    class Meta:
        ordering = ['id']
        verbose_name = 'Page'
        verbose_name_plural = 'Page'

    def scores(self):
        pass


class RecommendedActivities (models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    data = models.DateField()
    systemRating = models.IntegerField()
    expertRating = models.IntegerField()
    accepted = models.BooleanField()
    expertConsideration = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Atividades Recomendadas'
        verbose_name_plural = 'Atividades Recomendadas'
