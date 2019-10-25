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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers


from activities_section.api.viewsets import CharacteristicViewSet, BenefitViewSet, RestrictionViewSet, TypeViewSet, \
    ActivityViewSet
from institution_section.api.viewsets import AddressViewSet, ContactViewSet, LocationViewSet, InstructorViewSet, \
    ResponsibleViewSet, InstitutionViewSet
from page_section.api.viewsets import  NegativeAttitudesAgingViewSet, CognitionDeficitViewSet, DepressionViewSet,\
    PsychologicalAspectsViewSet, BiologicalAspectsViewSet, SensoryDeficitViewSet, FunctionalDisabilityViewSet,\
    MalnutritionViewSet, CardiovascularFactorsViewSet, MisuseMedicationsViewSet, SocialAspectsViewSet,\
    LowSocialSupportViewSet, EnvironmentalProblemsViewSet, ViolenceViewSet, MultidisciplinaryDomainViewSet,\
    FallsViewSet, PageViewSet
from participant_section.api.viewsets import ParticipantViewSet, IncomeViewSet, ParticipantSocialMediaViewSet, \
    MaritalStatusViewSet, SchoolingViewSet, ProfessionalsActivitiesViewSet, ReligionViewSet, ParticipantSituationViewSet
from recommendation_system import settings
from recommender_section.api.viewsets import OfferViewSet
from assessment_section.api.viewsets import *
from experts_section.api.viewsets import ExpertViewSet, ExpertiseViewSet
from health_section.api.viewsets import DiseasesViewSet, TherapeuticClassViewSet, HealthProblemsViewSet,\
    MedicinesViewSet, FracturesViewSet
from drinks_section.api.viewsets import DrinksViewSet, IngestedDrinksViewSet
from page_section.views import testar, abas, grava_page, grava_demanda, testa_grafico
from page_section import views as page_view
from drinks_section.api.viewsets import *


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
router.register(r'cognitionDeficit', CognitionDeficitViewSet, base_name='cognitionDeficit')
router.register(r'depression', DepressionViewSet, base_name='depression')
router.register(r'psychologicalAspects', PsychologicalAspectsViewSet, base_name='psychologicalAspects')
router.register(r'biologicalAspects', BiologicalAspectsViewSet, base_name='biologicalAspects')
router.register(r'sensoryDeficit', SensoryDeficitViewSet, base_name='sensoryDeficit')
router.register(r'functionalDisability', FunctionalDisabilityViewSet, base_name='functionalDisability')
router.register(r'malnutrition', MalnutritionViewSet, base_name='malnutrition')
router.register(r'cardiovascularFactors', CardiovascularFactorsViewSet, base_name='cardiovascularFactors')
router.register(r'misuseMedications', MisuseMedicationsViewSet, base_name='misuseMedications')
router.register(r'socialAspects', SocialAspectsViewSet, base_name='socialAspects')
router.register(r'lowSocialSupport', LowSocialSupportViewSet, base_name='lowSocialSupport')
router.register(r'environmentalProblems', EnvironmentalProblemsViewSet, base_name='environmentalProblems')
router.register(r'violence', ViolenceViewSet, base_name='violence')
router.register(r'multidisciplinaryDomain', MultidisciplinaryDomainViewSet, base_name='multidisciplinaryDomain')
router.register(r'falls', FallsViewSet, base_name='falls')
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

# assessment_section    path('grava_page',grava_page,name='grava_page'),
router.register(r'demands_problems', DemandsProblemsViewSet, base_name='demands_problems')
router.register(r'actions', ActionsViewSet, base_name='actions')
router.register(r'services', ServicesViewSet, base_name='services')
router.register(r'goals', GoalsViewSet, base_name='goals')
router.register(r'actions_planning', ActionsPlanningViewSet, base_name='assessments_controls')
router.register(r'actions_implementation_coordenation', ActionsImplementationCoordenationViewSet, base_name='expert_assessment')
router.register(r'reassessment_control', ReassessmentControlViewSet , base_name='actions_implementation')
router.register(r'demand_map', DemandMapViewSet , base_name='actions_implementation')
# experts_section
router.register(r'expertises', ExpertiseViewSet, base_name='expertise')
router.register(r'experts', ExpertViewSet, base_name='expert')

# health_section
router.register(r'diseases', DiseasesViewSet, base_name='diseases')
router.register(r'therapeuticClass', TherapeuticClassViewSet, base_name='therapeuticClass')
router.register(r'healthProblems', HealthProblemsViewSet, base_name='healthProblems')
router.register(r'medicines', MedicinesViewSet, base_name='medicines')
router.register(r'fractures', FracturesViewSet, base_name='fractures')

# drinks_section
router.register(r'drinks', DrinksViewSet, base_name='drinks')
router.register(r'ingestedDrinks',IngestedDrinksViewSet, base_name='ingestedDrinks')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('home/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="vazio"),
    path('teste/', testar,name='testar'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('abas',abas,name='abas'),
    path('grava_page',grava_page,name='grava_page'),
    path('grava_demanda',grava_demanda,name='grava_demanda'),
    path('testa_grafico',testa_grafico,name='testa_grafico'),
#    path('page/', PageViewSet, name='page'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
