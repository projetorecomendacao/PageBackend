from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def testar(request):
    depressionForm = DepressionForm()
    cognitionDeficitForms = CognitionDeficitForms ()
    negativeAttitudesAgingForms = NegativeAttitudesAgingForms ()
    psychologicalAspectsForm = PsychologicalAspectsForm()
    sensoryDeficitForm = SensoryDeficitForm()
    functionalDisabilityForm = FunctionalDisabilityForm()
    malnutritionForm = MalnutritionForm()
    cardiovascularFactorsForm = CardiovascularFactorsForm()
    misuseMedicationsForm = MisuseMedicationsForm()
    misuseMedicationsForm42 = MisuseMedicationsForm42()
    misuseMedicationsForm43 = MisuseMedicationsForm43()
    biologicalAspectsForm = BiologicalAspectsForm()
    lowSocialSupportForm = LowSocialSupportForm()
    environmentalProblemsForm = EnvironmentalProblemsForm()
    violenceForm = ViolenceForm()
    socialAspectsForm = SocialAspectsForm ()
    fallsForm = FallsForm()
    multidisciplinaryDomainForm = MultidisciplinaryDomainForm()
    pageForm = PageForm()

    return render(request, 'teste.html', {'cognition':cognitionDeficitForms,'depression': depressionForm, 'negative':
                  negativeAttitudesAgingForms, 'psychological': psychologicalAspectsForm,
                  'sensory' : sensoryDeficitForm, 'functional' : functionalDisabilityForm, 'malnutrition': malnutritionForm,
                  'cardiovascular' : cardiovascularFactorsForm, 'biological':biologicalAspectsForm,
                  'low_social' : lowSocialSupportForm, 'environmental': environmentalProblemsForm,
                  'violence' : violenceForm, 'social' : socialAspectsForm, 'falls' : fallsForm,
                  'multidisciplinary': multidisciplinaryDomainForm, 'page' : pageForm, 'misuse42' : misuseMedicationsForm42,
                   'misuse43': misuseMedicationsForm43, 'misuse' : misuseMedicationsForm })
