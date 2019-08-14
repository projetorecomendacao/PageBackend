from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from page_section.models import DA_Attitudes, DB_LifeQuality, DC_Senses, DD_Malnutrition, DE_FunctionalCapacity, \
    DF_Depression, DG_Cognition, DH_CardiovascularFactors, DI_MedicationManagement, DJ_Ambient, DK_Falls, \
    DL_Violence, DM_SocialVulnerability, DN_Fragility, Page
from page_section.api.serializers import DA_AttitudesSerializer, DB_LifeQualitySerializer, DC_SensesSerializer, \
    DD_MalnutritionSerializer, DE_FunctionalCapacitySerializer, DF_DepressionSerializer, DG_CognitionSerializer, \
    DH_CardiovascularFactorsSerializer, DI_MedicationsManagementSerializer, DJ_AmbientSerializer, DK_FallsSerializer, \
    DL_ViolenceSerializer, DM_SocialVulnerabilitySerializer, DN_FragilitySerializer, PageSerializer


class DA_AttitudesViewSet(ModelViewSet):
    queryset = DA_Attitudes.objects.all()
    serializer_class = DA_AttitudesSerializer


class DB_LifeQualityViewSet(ModelViewSet):
    queryset = DB_LifeQuality.objects.all()
    serializer_class = DB_LifeQualitySerializer


class DC_SensesViewSet(ModelViewSet):
    queryset = DC_Senses.objects.all()
    serializer_class = DC_SensesSerializer


class DD_MalnutritionViewSet(ModelViewSet):
    queryset = DD_Malnutrition.objects.all()
    serializer_class = DD_MalnutritionSerializer


class DE_FunctionalCapacityViewSet(ModelViewSet):
    queryset = DE_FunctionalCapacity.objects.all()
    serializer_class = DE_FunctionalCapacitySerializer


class DF_DepressionViewSet(ModelViewSet):
    queryset = DF_Depression.objects.all()
    serializer_class = DF_DepressionSerializer


class DG_CognitionViewSet(ModelViewSet):
    queryset = DG_Cognition.objects.all()
    serializer_class = DG_CognitionSerializer


class DH_CardiovascularFactorsViewSet(ModelViewSet):
    queryset = DH_CardiovascularFactors.objects.all()
    serializer_class = DH_CardiovascularFactorsSerializer


class DI_MedicationManagementViewSet(ModelViewSet):
    queryset = DI_MedicationManagement.objects.all()
    serializer_class = DI_MedicationsManagementSerializer


class DJ_AmbientViewSet(ModelViewSet):
    queryset = DJ_Ambient.objects.all()
    serializer_class = DJ_AmbientSerializer


class DK_FallsViewSet(ModelViewSet):
    queryset = DK_Falls.objects.all()
    serializer_class = DK_FallsSerializer


class DL_ViolenceViewSet(ModelViewSet):
    queryset = DL_Violence.objects.all()
    serializer_class = DL_ViolenceSerializer


class DM_SocialVulnerabilityViewSet(ModelViewSet):
    queryset = DM_SocialVulnerability.objects.all()
    serializer_class = DM_SocialVulnerabilitySerializer


class DN_FragilityViewSet(ModelViewSet):
    queryset = DN_Fragility.objects.all()
    serializer_class = DN_FragilitySerializer


class PageViewSet (ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
