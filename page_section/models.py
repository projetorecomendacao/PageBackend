from django.db import models

from health_section.models import Diseases, Medicines, HealthProblems, Fractures
from review_section.models import Offers
from drinks_section.models import IngestedDrinks
from assessment_section.models import ExpertAssessment
from experts_section.models import Gerontologist

class Options():
    CHOICES = [
        ["S", "Sim"],
        ["N", "Não"]
    ]


# Begin psychological aspects
class CognitionDeficit (models.Model):
    q1_memory_good_like_before = models.CharField("1. O(A) senhor(a) considera que sua memória é tão boa quanto antes?", max_length=1,default="N",choices=Options.CHOICES)
    q2_memory_test = models.CharField("2.Memória", max_length=1,default="N",choices=Options.CHOICES)
    q3_language_function_attention = models.CharField("3.Linguagem, função executiva e atenção", max_length=1, default="N", choices=Options.CHOICES)
    q4_visospatial_ability = models.CharField("4. Habilidade visuoespacial", max_length=1, default="N", choices=Options.CHOICES)
    q4_visospatial_ability_score = models.IntegerField("4. Habilidade visuoespacial - Pontuação", default=0)
    q5_praxia = models.CharField("5.Praxia", max_length=1,default="N",choices=Options.CHOICES)
    q6_memory_test = models.CharField("6.Memória", max_length=1,default="N",choices=Options.CHOICES)
    need_investigation = models.CharField("Necessita Investigação?", max_length=1,default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=6)


    def score(self):
        pass

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class AgingAspects (models.Model):
    description: models.CharField(max_length=60)

    class Meta:
        ordering = ['id']


class NegativeAttitudesAging (models.Model):
    q7_age_self_perception = models.IntegerField("7.Que idade o(a) senhor(a) sente ter? ", blank=True, null=True)
    q7_age_self_perception_why = models.TextField("7. Por quê?", blank=True, null=True)
    q7_age_self_perception_analyze = models.CharField("7. O idoso se sente mais velho do que realmente é?", max_length=1, default="N", choices=Options.CHOICES)
    q8_aging_positive_points = models.ManyToManyField(AgingAspects, related_name='PositivePoints', blank=True, verbose_name="Aspectos positivos Envelhecimento")
    q8_aging_negative_points = models.ManyToManyField(AgingAspects, related_name='NegativePoints', blank=True, verbose_name="Aspectos positivos Envelhecimento")
    q8_aging_analyse = models.CharField("8. É perceptível uma visão mais negativa da velhice? ", max_length=1, default="N", choices=Options.CHOICES)
    need_investigation = models.CharField("Necessita Investigação?", max_length=1,default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=2)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class Depression (models.Model):
    q9_satisfied_with_life = models.CharField("9.De modo Geral Está Satisfeito com a vida?", max_length=1,default="N",choices=Options.CHOICES)
    q10_frequently_sad = models.CharField("10. O(A) senhor(a) se sente triste com frequência?", max_length=1,default="N",choices=Options.CHOICES)
    q11_stopped_doing_things = models.CharField("11. O(A) senhor(a) abandonou muitas coisas que fazia ou gostava de fazer?",max_length=1,default="N",choices=Options.CHOICES )
    q12_fear_bad_things_happen = models.CharField("12. O(A) senhor(a) tem medo que algum mal vá lhe acontecer?", max_length=1,default="N",choices=Options.CHOICES)
    q13_impatient_disquiet = models.CharField("13. O(A) senhor(a) se sente impaciente e agitado(a) com frequência?", max_length=1,default="N",choices=Options.CHOICES)
    q14_concentration_problem = models.CharField("14. O(A) senhor(a) tem dificuldade em se concentar?",max_length=1, default="N",choices=Options.CHOICES)
    need_investigation = models.CharField("Necessita Investigação?",max_length=1, default="N",choices=Options.CHOICES)
    max_score = models.IntegerField(default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class PsychologicalAspects (models.Model):
    cognition_deficit = models.OneToOneField(CognitionDeficit, on_delete=models.CASCADE, null=True)
    negative_attitudes_aging = models.OneToOneField(NegativeAttitudesAging, on_delete=models.CASCADE, null=True)
    depression = models.OneToOneField(Depression,  on_delete=models.CASCADE, null=True)
    comments = models.TextField("Observações sobre o bloco Psicológico")
    max_score = models.IntegerField(default=14)

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

    def score(self):
        pass
# End psychological aspects


# Begin Biological Aspects
class SensoryDeficit(models.Model):
    q15VisionProblems = models.BooleanField()
    q16HearingProblems = models.BooleanField()
    q17TasteProblems = models.BooleanField()
    q18SensesProblems = models.BooleanField()
    q19InteractionProblems = models.BooleanField()
    maxScore = models.IntegerField(default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class FunctionalDisability (models.Model):
    q20ToShop = models.BooleanField()
    q21UseTransport = models.BooleanField()
    q22ToCook = models.BooleanField()
    q23UseTelephone = models.BooleanField()
    q24DressUp = models.BooleanField()
    q25TakeShower = models.BooleanField()
    maxScore = models.IntegerField(default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class Malnutrition (models.Model):
    d26YourselfMalnourished = models.BooleanField()
    d27ChewingMouthProblems = models.BooleanField()
    d28Less3MealDaily = models.BooleanField()
    d29DecreasesAmountFood = models.BooleanField()
    d30LostWeightNoReason = models.BooleanField()
    d30LostWeightNoReasonAmount = models.IntegerField()
    d31StressIllnessHospitalization = models.BooleanField()
    q32BMI_Less22 = models.BooleanField()  # Usar cálculo de BMI do participante
    maxScore = models.IntegerField(default=6)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class CardiovascularFactors (models.Model):
    q33DCVFamiliarHistory = models.BooleanField()
    q34Hypertension = models.BooleanField()
    q35UncontrolledDiabetes = models.BooleanField()
    q35UnknownValueGlycemia = models.BooleanField()
    q36Cholesterol = models.BooleanField()
    q36UnknownValueCT_HDL = models.BooleanField()
    q37Smoker = models.BooleanField()
    q38Practice150MinutesExercises = models.BooleanField()
    q39HealthyEating = models.BooleanField()
    q40AlcoholIngestedLastWeek = models.ForeignKey(IngestedDrinks, on_delete=models.CASCADE, null=True)
    q41BMI_Obesity = models.BooleanField()  # Usar cálculo do BMI de participante
    maxScore = models.IntegerField(default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class MisuseMedications (models.Model):
    q42DiseasesLast5Years = models.ManyToManyField(Diseases, related_name='patients', blank=True)
    q43HealthProblems = models.ManyToManyField(HealthProblems, related_name='patients', blank=True)
    q44AmountDiagnostics = models.IntegerField()
    q45Medicines = models.ManyToManyField(Medicines, related_name='patients', blank=True)
    q46MedicinesIncrease = models.BooleanField()
    q47KnowMedicines = models.BooleanField ()
    q48MedicationsPrecribed = models.BooleanField()
    q49MedicineMedicalAdvice = models.BooleanField()
    q50AlreadyStoppedMedicines = models.BooleanField()
    q51SelfMedication = models.BooleanField()
    q52InappropriateMedication = models.BooleanField()
    q53RiskAdverseReaction = models.BooleanField()
    maxScore = models.IntegerField(default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class BiologicalAspects (models.Model):
    sensoryDeficit = models.OneToOneField(SensoryDeficit, on_delete= models.CASCADE)
    functionalDisability = models.OneToOneField(FunctionalDisability, on_delete=models.CASCADE)
    malNutrition = models.OneToOneField(Malnutrition, on_delete=models.CASCADE)
    cardiovascularFactors = models.OneToOneField(CardiovascularFactors, on_delete=models.CASCADE)
    misuseMedications = models.OneToOneField(MisuseMedications, on_delete= models.CASCADE)
    comments = models.TextField()
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        for score in (self.sensoryDeficit, self.functionalDisability, self.malNutrition,
                      self.cardiovascularFactors, self.misuseMedications):
            max_score += score.maxScore
        self.maxScore = max_score

    class Meta:
        ordering = ['id']

    def score(self):
        pass
# End Biological Aspects


# Begin Social Aspects
class LowSocialSupport (models.Model):
    q54Spouse = models.BooleanField()
    q54Mother = models.BooleanField()
    q53Father = models.BooleanField()
    q54Brothers = models.IntegerField()
    q54Children = models.IntegerField()
    q54GranChildren = models.IntegerField()
    q55MeetFamilyFriends = models.BooleanField()
    q56ParticipateFamilyDecisions = models.BooleanField()
    q57SatisfiedFamilyRelationship = models.BooleanField()
    q58HelpedIfNeedMoney = models.BooleanField()
    q59SomeoneHelpsIfNeed = models.BooleanField()
    q60SomeoneToHaveFun = models.BooleanField()
    q61ParticipateSocialEvents = models.BooleanField()
    q62RegularyHealtServices = models.BooleanField()
    maxScore = models.IntegerField(default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class EnvironmentalProblems (models.Model):
    # Internal environment
    q63EstableFurniture = models.BooleanField()
    q64LooseObjectsCarpets = models.BooleanField()
    q65SlipperyFloor = models.BooleanField()
    Q66HandrailOnStairs = models.BooleanField()
    q67LightedStairs = models.BooleanField()
    q68SuitableStairsSteps = models.BooleanField()
    q69NonSlipperyCarpet = models.BooleanField()

    # riskBehavior
    q70GetOnStool = models.BooleanField()
    q71TurnLightsOff = models.BooleanField()
    q72SafeShoes = models.BooleanField()

    # externalEnvironment
    q73ManicureSidewalks = models.BooleanField()
    q74PublicTransportAccess = models.BooleanField()
    q75CommerceAccess = models.BooleanField()
    q76EasePlasewalking = models.BooleanField()
    q77FunAccess = models.BooleanField()
    q78Safety = models.BooleanField()

    maxScore = models.IntegerField(default=16)

    def investigate(self):
        pass

    def score(self):
        pass

    def calcular(self):
        pass

    class Meta:
        ordering = ['id']


class Violence (models.Model):
    q79AfraidClosePerson = models.BooleanField()
    q80FeelsAbandoned = models.BooleanField()
    q81Forced = models.BooleanField()
    q82Assauteld = models.BooleanField()
    q83InNeed = models.BooleanField()
    q84SomeoneUsedMoney = models.BooleanField()
    q85TouchedWithoutPermission = models.BooleanField()
    q86DontTakeCareHealth = models.BooleanField()
    maxScore = models.IntegerField(default=8)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class SocialAspects (models.Model):
    lowSocialSupport = models.OneToOneField(LowSocialSupport, on_delete=models.CASCADE, null=True)
    environmentalProblems = models.OneToOneField(EnvironmentalProblems, on_delete=models.CASCADE, null=True)
    violence = models.OneToOneField(Violence, on_delete=models.CASCADE, null=True)
    comments = models.TextField()
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        for score in (self.lowSocialSupport, self.environmentalProblems, self.violence):
            max_score += score.maxScore
        self.maxScore = max_score

    class Meta:
        ordering = ['id']

    def score(self):
        pass
# End Social Aspects


# Begin Multidisciplinary Domain
class Falls (models.Model):
    q87FallsLastYear = models.BooleanField()
    q88AmountFallsLastYear = models.IntegerField()
    q89FracturesDueToFalls = models.BooleanField()
    q89FracturesList = models.ForeignKey(Fractures, on_delete=models.CASCADE, null=True)
    q90Strength_MMII = models.BooleanField()
    q91Equilibrium = models.BooleanField()
    q92OlderThan75 = models.BooleanField()
    q93Female = models.BooleanField()
    q94CognitiveAlterations = models.BooleanField()
    q95AVDsCommitment = models.BooleanField()
    q96VisualDeficit = models.BooleanField()
    q97DomesticRisks = models.BooleanField()
    q98BehaviorRisk = models.BooleanField()
    q99Inactivity = models.BooleanField()
    q100PriorAVE = models.BooleanField()
    q101PsychotropicMedicationsUse = models.BooleanField()
    q102HasDiseases = models.BooleanField()
    maxScore = models.IntegerField(default=8)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class MultidisciplinaryDomain (models.Model):
    falls = models.OneToOneField(Falls, on_delete=models.CASCADE, null=True)
    comments = models.TextField()
    maxScore = models.IntegerField(default=8)

    def investigate(self):
        pass

    def score(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        for score in (self.falls,):
            max_score += score.maxScore
        self.maxScore = max_score

    class Meta:
        ordering = ['id']
# End Multidisciplinary Domain


class DemandMap (models.Model):
    dm3_unmet_demands = models.TextField(null=True)
    gerontologist_assessment =  models.TextField(null=True)

    def d1_domain_contribution_calculation(self):
        pass

    def d2_dimension_contribution_calculation(self):
        pass


class Page (models.Model):
    gerontologist = models.ForeignKey(Gerontologist, on_delete=models.CASCADE, null=True)
    date = models.DateField("Data da Entrevista", null="True")
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null="True")
    p1_self_health_report = models.TextField("Auto Relato de Saúde - Como o senhor(a)", null=True)
    #Dimensões do Page
    psychologicalAspects = models.OneToOneField(PsychologicalAspects, on_delete=models.CASCADE, null=True)
    biologicalAspects = models.OneToOneField(BiologicalAspects, on_delete=models.CASCADE, null=True)
    socialAspects = models.OneToOneField(SocialAspects, on_delete=models.CASCADE, null=True)
    multidisciplinaryDomain = models.OneToOneField(MultidisciplinaryDomain, on_delete=models.CASCADE, null=True)
    #Mapa de Demandas
    demandMap = models.OneToOneField(DemandMap,on_delete=models.CASCADE, null=True)
    #Avaliação Multidisciplinar
    expertAssessment = models.ForeignKey(ExpertAssessment, on_delete=models.CASCADE, null=True)
    #Atividades Recomendadas
    recommendedActivities = models.ManyToManyField(Offers,
                                                   through='RecommendedActivities',
                                                   related_name='page',
                                                   blank=True
                                                   )

    class Meta:
        ordering = ['id']

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
