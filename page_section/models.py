from django.db import models

from health_section.models import Diseases, Medicines, HealthProblems, Fractures
from review_section.models import Offers
from drinks_section.models import IngestedDrinks
from assessment_section.models import ExpertAssessment

# Begin psychological aspects

class CognitionDeficit (models.Model):
    q1MemoryGoodLikeBefore = models.BooleanField()
    q2MemoryTest = models.BooleanField()
    q3LanguageFunctionAttention = models.BooleanField()
    q4VisospatialAbility =models.BooleanField()
    q4VisospatialAbilityScore = models.IntegerField()
    q5Praxia = models.BooleanField ()
    q6MemoryTest = models.BooleanField ()
    maxScore = models.IntegerField()

    def score(self):
        pass

    def __init__(self):

        self.MaxScore = 6

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class AgingAspects (models.Model):
    description: models.CharField(max_length=60)

    class Meta:
        ordering = ['id']

class NegativeAttitudesAging (models.Model):
    q7AgeSelfPerception = models.IntegerField()
    q7AgeSelfPerceptionWhy = models.TextField()
    q7AgeSelfPerceptionAnalyze = models.BooleanField()
    q8AgingPositivePoints = models.ManyToManyField(AgingAspects,related_name='PositivePoints', null=True)
    q8AgingNegativePoints = models.ManyToManyField(AgingAspects,related_name='NegativePoints', null=True)
    q8AgingAnalyse = models.BooleanField()
    maxScore = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 2

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']

class Depression (models.Model):
    description = models.TextField()
    q9SatisfiedWithLife = models.BooleanField()
    q10FrequentlySad = models.BooleanField()
    q11StoppedDoingThings = models.BooleanField()
    q12FearBadThingsHappen = models.BooleanField()
    q13ImpatientDisquiet = models.BooleanField()
    q14ConcentrationProblem = models.BooleanField()
    maxScore = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 6

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class PsychologicalAspects (models.Model):
    cognitionDeficit = models.OneToOneField(CognitionDeficit, on_delete= models.CASCADE, null=True)
    negativeAttitudesAging = models.OneToOneField(NegativeAttitudesAging,  on_delete= models.CASCADE, null=True)
    depression = models.OneToOneField(Depression,  on_delete= models.CASCADE, null=True)
    comments = models.TextField()
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 6

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
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 6

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
    q32BMI_Less22 = models.BooleanField() #Usar cálculo de BMI do participante
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 6

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
    q41BMI_Obesity = models.BooleanField() #Usar cálculo do BMI de participante
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 9

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
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 9

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

    class Meta:
        ordering = ['id']

    def score(self):
        pass

# End Biological Aspects

# Begin Social Aspects

class LowSocialSupport (models.Model):
    q54Spouse = models.BooleanField()
    q54Mother = models.BooleanField()
    q53Father = models.BooleanField ()
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
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 9

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class InternalEnvironment (models.Model):
    q63EstableFurniture = models.BooleanField()
    q64LooseObjectsCarpets = models.BooleanField()
    q65SlipperyFloor = models.BooleanField()
    Q66HandrailOnStairs = models.BooleanField()
    q67LightedStairs = models.BooleanField()
    q68SuitableStairsSteps = models.BooleanField()
    q69NonSlipperyCarpet = models.BooleanField()

    def calcular(self):
        pass

class RiskBehavior (models.Model):
    q70GetOnStool = models.BooleanField()
    q71TurnLightsOff = models.BooleanField()
    q72SafeShoes = models.BooleanField()

    def calcular(self):
        pass

class ExternalEnvironment (models.Model):
    q73ManicureSidewalks = models.BooleanField()
    q74PublicTransportAccess = models.BooleanField()
    q75CommerceAccess = models.BooleanField()
    q76EasePlasewalking = models.BooleanField()
    q77FunAccess = models.BooleanField()
    q78Safety = models.BooleanField()

    def calcular(self):
        pass


class EnvironmentalProblems (models.Model):
    internalEnvironment = models.OneToOneField(InternalEnvironment, on_delete=models.CASCADE, null=True)
    riskBehavior = models.OneToOneField(RiskBehavior, on_delete=models.CASCADE)
    externalEnvironment = models.OneToOneField(ExternalEnvironment, on_delete=models.CASCADE, null=True)
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 16

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class Violence (models.Model):
    q79AfraidClosePerson = models.BooleanField()
    q80FeelsAbandoned = models.BooleanField()
    q81Forced = models.BooleanField()
    q82Assauteld = models.BooleanField()
    q83InNeed = models.BooleanField()
    q84SomeoneUsedMoney = models.BooleanField()
    q85TouchedWithoutPermission = models.BooleanField()
    q86DontTakeCareHealth = models.BooleanField()
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 8

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
        self.MaxScore = 8

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
    q89FracturesList = models.ForeignKey(Fractures,on_delete=models.CASCADE, null=True)
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
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 8

    class Meta:
        ordering = ['id']

    def score(self):
        pass


class MultidisciplinaryDomain (models.Model):
    falls = models.OneToOneField (Falls, on_delete=models.CASCADE, null=True)
    comments = models.TextField()
    maxScore = models.IntegerField()

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MaxScore = 8

    class Meta:
        ordering = ['id']

    def score(self):
        pass

# End Multidisciplinary Domain


class Page (models.Model):
    date = models.DateField()
    selfHealthReport = models.TextField(null=True)
    unmetDemands = models.TextField(null=True)
    psychologicalAspects = models.OneToOneField(PsychologicalAspects, on_delete=models.CASCADE, null=True)
    biologicalAspects = models.OneToOneField(BiologicalAspects, on_delete=models.CASCADE, null=True)
    socialAspects = models.OneToOneField(SocialAspects, on_delete=models.CASCADE, null=True)
    multidisciplinaryDomain = models.OneToOneField(MultidisciplinaryDomain, on_delete=models.CASCADE, null=True)
    expertAssessment = models.ForeignKey(ExpertAssessment, on_delete=models.CASCADE, null=True)
    recommendedActivities = models.ManyToManyField(Offers,through='RecommendedActivities',related_name='page', null=True)

    class Meta:
        ordering = ['id']

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