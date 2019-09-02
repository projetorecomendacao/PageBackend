from rest_framework.serializers import ModelSerializer
from page_section.models import NegativeAttitudesAging, CognitionDeficit, Depression, PsychologicalAspects, \
     BiologicalAspects, SensoryDeficit, FunctionalDisability, Malnutrition, CardiovascularFactors, MisuseMedications, \
     SocialAspects, LowSocialSupport, EnvironmentalProblems, InternalEnvironment, RiskBehavior, ExternalEnvironment, Violence,\
     MultidisciplinaryDomain, Falls, \
     Page

class NegativeAttitudesAgingSerializer (ModelSerializer):
    class Meta:
        model = NegativeAttitudesAging
        fields = '__all__'

class CognitionDeficitSerializer (ModelSerializer):
    class Meta:
        model = CognitionDeficit
        fields = '__all__'

class DepressionSerializer (ModelSerializer):
    class Meta:
        model = Depression
        fields = '__all__'

class PsychologicalAspectsSerializer (ModelSerializer):
    class Meta:
        model = PsychologicalAspects,
        fields = '__all__'

class BiologicalAspectsSerializer (ModelSerializer):
    class Meta:
        model = BiologicalAspects
        fields = '__all__'

class SensoryDeficitSerializer(ModelSerializer):
    class Meta:
        model = SensoryDeficit
        fields = '__all__'

class FunctionalDisabilitySerializer(ModelSerializer):
    class Meta:
        model = FunctionalDisability
        fields = '__all__'

class MalnutritionSerializer(ModelSerializer):
    class Meta:
        model = Malnutrition
        fields = '__all__'

class CardiovascularFactorsSerializer(ModelSerializer):
    class Meta:
        model = CardiovascularFactors
        fields = '__all__'

class MisuseMedicationsSerializer(ModelSerializer):
    class Meta:
        model = MisuseMedications
        fields = '__all__'

class SocialAspectsSerializer (ModelSerializer):
    class Meta:
        model = SocialAspects
        fields = '__all__'

class LowSocialSupportSerializer (ModelSerializer):
    class Meta:
        model = LowSocialSupport
        fields = '__all__'

class EnvironmentalProblemsSerializer (ModelSerializer):
    class Meta:
        model = EnvironmentalProblems
        fields = '__all__'

class InternalEnvironmentSerializer (ModelSerializer):
    class Meta:
        model = InternalEnvironment
        fields = '__all__'

class RiskBehaviorSerializer (ModelSerializer):
    class Meta:
        model = RiskBehavior
        fields = '__all__'

class ExternalEnvironmentSerializer (ModelSerializer):
    class Meta:
        model = ExternalEnvironment
        fields = '__all__'

class ViolenceSerializer (ModelSerializer):
    class Meta:
        model = Violence
        fields = '__all__'

class MultidisciplinaryDomainSerializer (ModelSerializer):
    class Meta:
        model = MultidisciplinaryDomain
        fields = '__all__'

class FallsSerializer (ModelSerializer):
    class Meta:
        model = Falls
        fields = '__all__'

class PageSerializer (ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
        depth = 1
