from rest_framework.serializers import ModelSerializer
from page_section.models import DA_Attitudes, DB_LifeQuality, DC_Senses, DD_Malnutrition, DE_FunctionalCapacity, \
    DF_Depression, DG_Cognition, DH_CardiovascularFactors, DI_MedicationManagement, DJ_Ambient, DK_Falls, \
    DL_Violence, DM_SocialVulnerability, DN_Fragility, Page


class DA_AttitudesSerializer (ModelSerializer):
    class Meta:
        model = DA_Attitudes
        fields = '__all__'


class DB_LifeQualitySerializer (ModelSerializer):
    class Meta:
        model = DB_LifeQuality
        fields = '__all__'


class DC_SensesSerializer (ModelSerializer):
    class Meta:
        model = DC_Senses
        fields = '__all__'


class DD_MalnutritionSerializer (ModelSerializer):
    class Meta:
        model = DD_Malnutrition
        fields = '__all__'


class DE_FunctionalCapacitySerializer (ModelSerializer):
    class Meta:
        model = DE_FunctionalCapacity
        fields = '__all__'


class DF_DepressionSerializer (ModelSerializer):
    class Meta:
        model = DF_Depression
        fields = '__all__'


class DG_CognitionSerializer (ModelSerializer):
    class Meta:
        model = DG_Cognition
        fields = '__all__'


class DH_CardiovascularFactorsSerializer (ModelSerializer):
    class Meta:
        model = DH_CardiovascularFactors
        fields = '__all__'


class DI_MedicationsManagementSerializer (ModelSerializer):
    class Meta:
        model = DI_MedicationManagement
        fields = '__all__'


class DJ_AmbientSerializer (ModelSerializer):
    class Meta:
        model = DJ_Ambient
        fields = '__all__'


class DK_FallsSerializer (ModelSerializer):
    class Meta:
        model = DK_Falls
        fields = '__all__'


class DL_ViolenceSerializer (ModelSerializer):
    class Meta:
        model = DL_Violence
        fields = '__all__'


class DM_SocialVulnerabilitySerializer (ModelSerializer):
    class Meta:
        model = DM_SocialVulnerability
        fields = '__all__'


class DN_FragilitySerializer (ModelSerializer):
    class Meta:
        model = DN_Fragility
        fields = '__all__'


class PageSerializer (ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
        depth = 1
