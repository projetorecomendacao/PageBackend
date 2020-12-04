from rest_framework.serializers import ModelSerializer

from experts_section.models import Expert
from page_usp_section.models_1_psicologico_usp import NegativeAttitudesAgingUsp, CognitionDeficitUsp, DepressionUsp, PsychologicalAspectsUsp
from page_usp_section.models_2_Biologicos_usp import BiologicalAspectsUsp, SensoryDeficitUsp, FunctionalDisabilityUsp, MalnutritionUsp, CardiovascularFactorsUsp, MisuseMedicationsUsp
from page_usp_section.models_3_sociais_usp import SocialAspectsUsp, LowSocialSupportUsp, EnvironmentalProblemsUsp, ViolenceUsp
from page_usp_section.models_4_multidimensional_usp import MultidisciplinaryDomainUsp, FallsUsp
from page_usp_section.models_0_page_usp import PageUsp, Avaliacao


class NegativeAttitudesAgingUspSerializer (ModelSerializer):
    class Meta:
        model = NegativeAttitudesAgingUsp
        fields = '__all__'


class CognitionDeficitUspSerializer (ModelSerializer):
    class Meta:
        model = CognitionDeficitUsp
        fields = '__all__'


class DepressionUspSerializer (ModelSerializer):
    class Meta:
        model = DepressionUsp
        fields = '__all__'


class PsychologicalAspectsUspSerializer (ModelSerializer):
    class Meta:
        model = PsychologicalAspectsUsp
        fields = '__all__'


class BiologicalAspectsUspSerializer (ModelSerializer):
    class Meta:
        model = BiologicalAspectsUsp
        fields = '__all__'


class SensoryDeficitUspSerializer(ModelSerializer):
    class Meta:
        model = SensoryDeficitUsp
        fields = '__all__'


class FunctionalDisabilityUspSerializer(ModelSerializer):
    class Meta:
        model = FunctionalDisabilityUsp
        fields = '__all__'


class MalnutritionUspSerializer(ModelSerializer):
    class Meta:
        model = MalnutritionUsp
        fields = '__all__'


class CardiovascularFactorsUspSerializer(ModelSerializer):
    class Meta:
        model = CardiovascularFactorsUsp
        fields = '__all__'


class MisuseMedicationsUspSerializer(ModelSerializer):
    class Meta:
        model = MisuseMedicationsUsp
        fields = '__all__'


class SocialAspectsUspSerializer (ModelSerializer):
    class Meta:
        model = SocialAspectsUsp
        fields = '__all__'


class LowSocialSupportUspSerializer (ModelSerializer):
    class Meta:
        model = LowSocialSupportUsp
        fields = '__all__'


class EnvironmentalProblemsUspSerializer (ModelSerializer):
    class Meta:
        model = EnvironmentalProblemsUsp
        fields = '__all__'


class ViolenceUspSerializer (ModelSerializer):
    class Meta:
        model = ViolenceUsp
        fields = '__all__'


class MultidisciplinaryDomainUspSerializer (ModelSerializer):
    class Meta:
        model = MultidisciplinaryDomainUsp
        fields = '__all__'


class FallsUspSerializer (ModelSerializer):
    class Meta:
        model = FallsUsp
        fields = '__all__'


class PageUspSerializer (ModelSerializer):
    class Meta:
        model = PageUsp
        fields = '__all__'

class AvaliacaoSerializer (ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
