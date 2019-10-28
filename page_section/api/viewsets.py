from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from page_section.models_1_psicologico import NegativeAttitudesAging, CognitionDeficit, Depression, PsychologicalAspects
from page_section.models_2_Biologicos import BiologicalAspects, SensoryDeficit, FunctionalDisability, Malnutrition, CardiovascularFactors, MisuseMedications
from page_section.models_3_sociais import SocialAspects, LowSocialSupport, EnvironmentalProblems, Violence
from page_section.models_4_multidimensional import MultidisciplinaryDomain, Falls
from page_section.models_0_page import Page
from page_section.api.serializers import NegativeAttitudesAgingSerializer, CognitionDeficitSerializer,\
    DepressionSerializer, PsychologicalAspectsSerializer, BiologicalAspectsSerializer, SensoryDeficitSerializer,\
    FunctionalDisabilitySerializer, MalnutritionSerializer, CardiovascularFactorsSerializer,\
    MisuseMedicationsSerializer, SocialAspectsSerializer, LowSocialSupportSerializer, EnvironmentalProblemsSerializer,\
    ViolenceSerializer, MultidisciplinaryDomainSerializer, FallsSerializer, PageSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert


class NegativeAttitudesAgingViewSet(CustomModelViewSet):
    queryset = NegativeAttitudesAging.objects.all()
    serializer_class = NegativeAttitudesAgingSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CognitionDeficitViewSet(CustomModelViewSet):
    queryset = CognitionDeficit.objects.all()
    serializer_class = CognitionDeficitSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class DepressionViewSet(CustomModelViewSet):
    queryset = Depression.objects.all()
    serializer_class = DepressionSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PsychologicalAspectsViewSet(CustomModelViewSet):
    queryset = PsychologicalAspects.objects.all()
    serializer_class = PsychologicalAspectsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class BiologicalAspectsViewSet(ModelViewSet):
    queryset = BiologicalAspects.objects.all()
    serializer_class = BiologicalAspectsSerializer


class SensoryDeficitViewSet(ModelViewSet):
    queryset = SensoryDeficit.objects.all()
    serializer_class = SensoryDeficitSerializer


class FunctionalDisabilityViewSet(ModelViewSet):
    queryset = FunctionalDisability.objects.all()
    serializer_class = FunctionalDisabilitySerializer


class MalnutritionViewSet(ModelViewSet):
    queryset = Malnutrition.objects.all()
    serializer_class = MalnutritionSerializer


class CardiovascularFactorsViewSet(ModelViewSet):
    queryset = CardiovascularFactors.objects.all()
    serializer_class = CardiovascularFactorsSerializer


class MisuseMedicationsViewSet(ModelViewSet):
    queryset = MisuseMedications.objects.all()
    serializer_class = MisuseMedicationsSerializer


class SocialAspectsViewSet(ModelViewSet):
    queryset = SocialAspects.objects.all()
    serializer_class = SocialAspectsSerializer


class LowSocialSupportViewSet(ModelViewSet):
    queryset = LowSocialSupport.objects.all()
    serializer_class = LowSocialSupportSerializer


class EnvironmentalProblemsViewSet(ModelViewSet):
    queryset = EnvironmentalProblems.objects.all()
    serializer_class = EnvironmentalProblemsSerializer


class ViolenceViewSet(ModelViewSet):
    queryset = Violence.objects.all()
    serializer_class = ViolenceSerializer


class MultidisciplinaryDomainViewSet(ModelViewSet):
    queryset = MultidisciplinaryDomain.objects.all()
    serializer_class = MultidisciplinaryDomainSerializer


class FallsViewSet(ModelViewSet):
    queryset = Falls.objects.all()
    serializer_class = FallsSerializer


class PageViewSet (ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def create(self, request, *args, **kwargs):

        pass
