"""recommendation_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from activities_section.api.viewsets import CharacteristicViewSet, BenefitViewSet, RestrictionViewSet, TypeViewSet, \
    ActivityViewSet
from institution_section.api.viewsets import AddressViewSet, ContactViewSet, LocationViewSet, InstructorViewSet, \
    ResponsibleViewSet, InstitutionViewSet
from page_section.api.viewsets import  NegativeAttitudesAgingViewSet, CognitionDeficitViewSet, DepressionViewSet, PsychologicalAspectsViewSet, \
     BiologicalAspectsViewSet, SensoryDeficitViewSet, FunctionalDisabilityViewSet, MalnutritionViewSet, CardiovascularFactorsViewSet, MisuseMedicationsViewSet, \
     SocialAspectsViewSet, LowSocialSupportViewSet, EnvironmentalProblemsViewSet, InternalEnvironmentViewSet, RiskBehaviorViewSet, ExternalEnvironmentViewSet, ViolenceViewSet,\
     MultidisciplinaryDomainViewSet, FallsViewSet, \
     PageViewSet
from participant_section.api.viewsets import ParticipantViewSet, IncomeViewSet, ParticipantSocialMediaViewSet, \
    MaritalStatusViewSet, SchoolingViewSet, ProfessionalsActivitiesViewSet, ReligionViewSet, ParticipantSituationViewSet
from review_section.api.viewsets import OfferViewSet, ReviewViewSet
from assessment_section.api.viewsets import DemandsProblemsViewSet, ActionsViewSet, ServicesViewSet, GoalsViewSet, AssessmentsControlViewSet, ExpertAssessmentViewSet, ActionsImplementationViewSet
from experts_section.api.viewsets import ExpertViewSet,ExpertiseViewSet
from health_section.api.viewsets import DiseasesViewSet, TherapeuticClassViewSet, HealthProblemsViewSet, MedicinesViewSet, FracturesViewSet
from drinks_section.api.viewsets import DrinksViewSet, IngestedDrinksViewSet


router = routers.DefaultRouter()

# activities_section
router.register(r'characteristics', CharacteristicViewSet, base_name='Characteristic')
router.register(r'benefits', BenefitViewSet, base_name='Benefit')
router.register(r'restrictions', RestrictionViewSet, base_name='Restriction')
router.register(r'types', TypeViewSet, base_name='Type')
router.register(r'activities', ActivityViewSet, base_name='Activity')

# institution_section
router.register(r'addresses', AddressViewSet, base_name='Address')
router.register(r'institutions', InstitutionViewSet, base_name='Institution')
router.register(r'locations', LocationViewSet, base_name='Location')
router.register(r'contacts', ContactViewSet, base_name='Contact')
router.register(r'instructors', InstructorViewSet, base_name='Instructor')
router.register(r'responsibles', ResponsibleViewSet, base_name='Responsible')

# page_section
router.register(r'negativeAttitudesAging', NegativeAttitudesAgingViewSet, base_name='negativeAttitudesAging')
router.register(r'cognitionDeficit',CognitionDeficitViewSet, base_name='cognitionDeficit')
router.register(r'depression',DepressionViewSet, base_name='depression')
router.register(r'psychologicalAspects',PsychologicalAspectsViewSet, base_name='psychologicalAspects')
router.register(r'biologicalAspects',BiologicalAspectsViewSet, base_name='biologicalAspects')
router.register(r'sensoryDeficit',SensoryDeficitViewSet, base_name='sensoryDeficit')
router.register(r'functionalDisability',FunctionalDisabilityViewSet, base_name='functionalDisability')
router.register(r'malnutrition',MalnutritionViewSet, base_name='malnutrition')
router.register(r'cardiovascularFactors',CardiovascularFactorsViewSet, base_name='cardiovascularFactors')
router.register(r'misuseMedications',MisuseMedicationsViewSet, base_name='misuseMedications')
router.register(r'socialAspects',SocialAspectsViewSet, base_name='socialAspects')
router.register(r'lowSocialSupport',LowSocialSupportViewSet, base_name='lowSocialSupport')
router.register(r'environmentalProblems',EnvironmentalProblemsViewSet, base_name='environmentalProblems')
router.register(r'internalEnvironment',InternalEnvironmentViewSet, base_name='internalEnvironment')
router.register(r'riskBehavior',RiskBehaviorViewSet, base_name='riskBehavior')
router.register(r'externalEnvironment',ExternalEnvironmentViewSet, base_name='externalEnvironment')
router.register(r'violence',ViolenceViewSet, base_name='violence')
router.register(r'multidisciplinaryDomain',MultidisciplinaryDomainViewSet, base_name='multidisciplinaryDomain')
router.register(r'falls',FallsViewSet, base_name='falls')
router.register(r'page', PageViewSet, base_name='page')

# participant_section
router.register(r'participants', ParticipantViewSet, base_name='DA_attitudes')
router.register(r'incomes', IncomeViewSet, base_name='DA_attitudes')
router.register(r'social_medias', ParticipantSocialMediaViewSet, base_name='DA_attitudes')
router.register(r'marital_status', MaritalStatusViewSet, base_name='DA_attitudes')
router.register(r'schooling', SchoolingViewSet, base_name='DA_attitudes')
router.register(r'professionals_activities', ProfessionalsActivitiesViewSet, base_name='DA_attitudes')
router.register(r'religions', ReligionViewSet, base_name='DA_attitudes')
router.register(r'participants_situations', ParticipantSituationViewSet, base_name='DA_attitudes')

# reviews_section
router.register(r'offers', OfferViewSet, base_name='Offers')
router.register(r'reviews', ReviewViewSet, base_name='Reviews')

# assessment_section
router.register(r'demands_problems', DemandsProblemsViewSet, base_name='demands_problems')
router.register(r'actions', ActionsViewSet, base_name='actions')
router.register(r'services', ServicesViewSet, base_name='services')
router.register(r'goals', GoalsViewSet, base_name='goals')
router.register(r'assessment_controls', AssessmentsControlViewSet, base_name='assessments_controls')
router.register(r'expert_assessment', ExpertAssessmentViewSet, base_name='expert_assessment')
router.register(r'actions_implementation', ActionsImplementationViewSet, base_name='actions_implementation')

# experts_section
router.register(r'expertise', ExpertiseViewSet, base_name='expertise')
router.register(r'expert', ExpertViewSet, base_name='expert')

#health_section
router.register(r'diseases',DiseasesViewSet,base_name='diseases')
router.register(r'therapeuticClass',TherapeuticClassViewSet,base_name='therapeuticClass')
router.register(r'healthProblems',HealthProblemsViewSet,base_name='healthProblems')
router.register(r'medicines',MedicinesViewSet,base_name='medicines')
router.register(r'fractures',FracturesViewSet,base_name='fractures')

#drinks_section
router.register(r'drinks', DrinksViewSet, base_name='drinks')
router.register(r'ingestedDrinks', IngestedDrinksViewSet, base_name='ingestedDrinks')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]


