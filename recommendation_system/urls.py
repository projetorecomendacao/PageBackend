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
from institution_section.api.viewsets import CidadeViewSet, AddressViewSet, \
     LocalsViewSet, ProfessionalViewSet, InstitutionViewSet, \
     AssistanceModalityViewSet, WebAddressViewSet, OffersViewSet, CapacityViewSet
from page_section.api.viewsets import  NegativeAttitudesAgingViewSet, CognitionDeficitViewSet, DepressionViewSet,\
    PsychologicalAspectsViewSet, BiologicalAspectsViewSet, SensoryDeficitViewSet, FunctionalDisabilityViewSet,\
    MalnutritionViewSet, CardiovascularFactorsViewSet, MisuseMedicationsViewSet, SocialAspectsViewSet,\
    LowSocialSupportViewSet, EnvironmentalProblemsViewSet, ViolenceViewSet, MultidisciplinaryDomainViewSet,\
    FallsViewSet, PageViewSet
from participant_section.api.viewsets import ParticipantViewSet, IncomeViewSet, ParticipantSocialMediaViewSet, \
    MaritalStatusViewSet, SchoolingViewSet, ProfessionalsActivitiesViewSet, ReligionViewSet, ParticipantSituationViewSet
from recommendation_system import settings
from assessment_section.api.viewsets import *
from experts_section.api.viewsets import ExpertViewSet, ExpertiseViewSet
from health_section.api.viewsets import DiseasesViewSet, TherapeuticClassViewSet, HealthProblemsViewSet,\
    MedicinesViewSet, FracturesViewSet
from drinks_section.api.viewsets import DrinksViewSet, IngestedDrinksViewSet
from page_section.views import testar, abas, grava_page, grava_demanda, testa_grafico
from page_section import views as page_view
from drinks_section.api.viewsets import *
from page_usp_section.api.viewsets import  NegativeAttitudesAgingViewSetUsp, CognitionDeficitViewSetUsp, DepressionViewSetUsp,\
    PsychologicalAspectsViewSetUsp, BiologicalAspectsViewSetUsp, SensoryDeficitViewSetUsp, FunctionalDisabilityViewSetUsp,\
    MalnutritionViewSetUsp, CardiovascularFactorsViewSetUsp, MisuseMedicationsViewSetUsp, SocialAspectsViewSetUsp,\
    LowSocialSupportViewSetUsp, EnvironmentalProblemsViewSetUsp, ViolenceViewSetUsp, MultidisciplinaryDomainViewSetUsp,\
    FallsViewSetUsp, PageViewSetUsp



router = routers.DefaultRouter()

# institution_section
router.register(r'cidades', CidadeViewSet, basename='Cidade')
router.register(r'addresses', AddressViewSet, basename='Address')
router.register(r'locals', LocalsViewSet, basename='Location')
router.register(r'professionals', ProfessionalViewSet, basename='Location')
router.register(r'institutions', InstitutionViewSet, basename='Institution')
router.register(r'assitancemodality', AssistanceModalityViewSet, basename='Assistance')
router.register(r'webaddress', WebAddressViewSet, basename='WebAddress')
router.register(r'offers', OffersViewSet, basename='Offers')
router.register(r'capacity', CapacityViewSet, basename='Capacity')


# activities_section
router.register(r'characteristics', CharacteristicViewSet, basename='Characteristic')
router.register(r'benefits', BenefitViewSet, basename='Benefit')
router.register(r'restrictions', RestrictionViewSet, basename='Restriction')
router.register(r'types', TypeViewSet, basename='Type')
router.register(r'activities', ActivityViewSet, basename='Activity')


# page_section
router.register(r'negativeAttitudesAging', NegativeAttitudesAgingViewSet, basename='negativeAttitudesAging')
router.register(r'cognitionDeficit', CognitionDeficitViewSet, basename='cognitionDeficit')
router.register(r'depression', DepressionViewSet, basename='depression')
router.register(r'psychologicalAspects', PsychologicalAspectsViewSet, basename='psychologicalAspects')
router.register(r'biologicalAspects', BiologicalAspectsViewSet, basename='biologicalAspects')
router.register(r'sensoryDeficit', SensoryDeficitViewSet, basename='sensoryDeficit')
router.register(r'functionalDisability', FunctionalDisabilityViewSet, basename='functionalDisability')
router.register(r'malnutrition', MalnutritionViewSet, basename='malnutrition')
router.register(r'cardiovascularFactors', CardiovascularFactorsViewSet, basename='cardiovascularFactors')
router.register(r'misuseMedications', MisuseMedicationsViewSet, basename='misuseMedications')
router.register(r'socialAspects', SocialAspectsViewSet, basename='socialAspects')
router.register(r'lowSocialSupport', LowSocialSupportViewSet, basename='lowSocialSupport')
router.register(r'environmentalProblems', EnvironmentalProblemsViewSet, basename='environmentalProblems')
router.register(r'violence', ViolenceViewSet, basename='violence')
router.register(r'multidisciplinaryDomain', MultidisciplinaryDomainViewSet, basename='multidisciplinaryDomain')
router.register(r'falls', FallsViewSet, basename='falls')
router.register(r'page', PageViewSet, basename='page')

# participant_section
router.register(r'participants', ParticipantViewSet, basename='DA_attitudes')
router.register(r'incomes', IncomeViewSet, basename='DA_attitudes')
router.register(r'social_medias', ParticipantSocialMediaViewSet, basename='DA_attitudes')
router.register(r'marital_status', MaritalStatusViewSet, basename='DA_attitudes')
router.register(r'schooling', SchoolingViewSet, basename='DA_attitudes')
router.register(r'professionals_activities', ProfessionalsActivitiesViewSet, basename='DA_attitudes')
router.register(r'religions', ReligionViewSet, basename='DA_attitudes')
router.register(r'participant_situations', ParticipantSituationViewSet, basename='DA_attitudes')


# assessment_section    path('grava_page',grava_page,name='grava_page'),
router.register(r'demands_problems', DemandsProblemsViewSet, basename='demands_problems')
router.register(r'actions', ActionsViewSet, basename='actions')
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'goals', GoalsViewSet, basename='goals')
router.register(r'actions_planning', ActionsPlanningViewSet, basename='assessments_controls')
router.register(r'actions_implementation_coordenation', ActionsImplementationCoordenationViewSet, basename='expert_assessment')
router.register(r'reassessment_control', ReassessmentControlViewSet , basename='actions_implementation')
router.register(r'demand_map', DemandMapViewSet , basename='actions_implementation')
# experts_section
router.register(r'expertises', ExpertiseViewSet, basename='expertise')
router.register(r'experts', ExpertViewSet, basename='expert')

# health_section
router.register(r'diseases', DiseasesViewSet, basename='diseases')
router.register(r'therapeuticClass', TherapeuticClassViewSet, basename='therapeuticClass')
router.register(r'healthProblems', HealthProblemsViewSet, basename='healthProblems')
router.register(r'medicines', MedicinesViewSet, basename='medicines')
router.register(r'fractures', FracturesViewSet, basename='fractures')

# drinks_section
router.register(r'drinks', DrinksViewSet, basename='drinks')
router.register(r'ingestedDrinks',IngestedDrinksViewSet, basename='ingestedDrinks')

# page_section_USP
router.register(r'negativeAttitudesAgingUsp', NegativeAttitudesAgingViewSetUsp, basename='negativeAttitudesAgingUsp')
router.register(r'cognitionDeficitUsp', CognitionDeficitViewSetUsp, basename='cognitionDeficitUsp')
router.register(r'depressionUsp', DepressionViewSetUsp, basename='depressionUsp')
router.register(r'psychologicalAspectsUsp', PsychologicalAspectsViewSetUsp, basename='psychologicalAspectsUsp')
router.register(r'biologicalAspectsUsp', BiologicalAspectsViewSetUsp, basename='biologicalAspectsUsp')
router.register(r'sensoryDeficitUsp', SensoryDeficitViewSetUsp, basename='sensoryDeficitUsp')
router.register(r'functionalDisabilityUsp', FunctionalDisabilityViewSetUsp, basename='functionalDisabilityUsp')
router.register(r'malnutritionUsp', MalnutritionViewSetUsp, basename='malnutritionUsp')
router.register(r'cardiovascularFactorsUsp', CardiovascularFactorsViewSetUsp, basename='cardiovascularFactorsUsp')
router.register(r'misuseMedicationsUsp', MisuseMedicationsViewSetUsp, basename='misuseMedicationsUsp')
router.register(r'socialAspectsUsp', SocialAspectsViewSetUsp, basename='socialAspectsUsp')
router.register(r'lowSocialSupportUsp', LowSocialSupportViewSetUsp, basename='lowSocialSupportUsp')
router.register(r'environmentalProblemsUsp', EnvironmentalProblemsViewSetUsp, basename='environmentalProblemsUsp')
router.register(r'violenceUsp', ViolenceViewSetUsp, basename='violenceUsp')
router.register(r'multidisciplinaryDomainUsp', MultidisciplinaryDomainViewSetUsp, basename='multidisciplinaryDomainUsp')
router.register(r'fallsUsp', FallsViewSetUsp, basename='fallsUsp')
router.register(r'pageUsp', PageViewSetUsp, basename='pageUsp')


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
