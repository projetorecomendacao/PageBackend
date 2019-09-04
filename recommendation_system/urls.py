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
from page_section.api.viewsets import DA_AttitudesViewSet, DB_LifeQualityViewSet, DC_SensesViewSet, \
    DD_MalnutritionViewSet, DE_FunctionalCapacityViewSet, DF_DepressionViewSet, DG_CognitionViewSet, \
    DH_CardiovascularFactorsViewSet, DI_MedicationManagementViewSet, DJ_AmbientViewSet, DK_FallsViewSet, \
    DL_ViolenceViewSet, DM_SocialVulnerabilityViewSet, DN_FragilityViewSet, PageViewSet
from participant_section.api.viewsets import ParticipantViewSet, IncomeViewSet, ParticipantSocialMediaViewSet, \
    MaritalStatusViewSet, SchoolingViewSet, ProfessionalsActivitiesViewSet, ReligionViewSet, ParticipantSituationViewSet
from review_section.api.viewsets import OfferViewSet, ReviewViewSet

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
router.register(r'DA_attitudes', DA_AttitudesViewSet, base_name='DA_attitudes')
router.register(r'DB_life_quality', DB_LifeQualityViewSet, base_name='DB_life_quality')
router.register(r'DC_senses', DC_SensesViewSet, base_name='DC_senses')
router.register(r'DD_malnutricion', DD_MalnutritionViewSet, base_name='DD_malnutricion')
router.register(r'DE_functional_capacity', DE_FunctionalCapacityViewSet, base_name='DE_functional_capacity')
router.register(r'DF_depression', DF_DepressionViewSet, base_name='DF_depression')
router.register(r'DG_cognition', DG_CognitionViewSet, base_name='DG_cognition')
router.register(r'DH_cardiovascular_factors', DH_CardiovascularFactorsViewSet, base_name='DH_cardiovascular_factors')
router.register(r'DI_medication_management', DI_MedicationManagementViewSet, base_name='DI_medication_management')
router.register(r'DJ_ambient', DJ_AmbientViewSet, base_name='DJ_ambient')
router.register(r'DK_falls', DK_FallsViewSet, base_name='DK_falls')
router.register(r'DL_violence', DL_ViolenceViewSet, base_name='DL_violence')
router.register(r'DM_social_vulnerability', DM_SocialVulnerabilityViewSet, base_name='DM_social_vulnerability')
router.register(r'DN_fragility', DN_FragilityViewSet, base_name='DN_fragility')
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

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls'))
]
