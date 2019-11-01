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


class BiologicalAspectsViewSet(CustomModelViewSet):
    queryset = BiologicalAspects.objects.all()
    serializer_class = BiologicalAspectsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SensoryDeficitViewSet(CustomModelViewSet):
    queryset = SensoryDeficit.objects.all()
    serializer_class = SensoryDeficitSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FunctionalDisabilityViewSet(CustomModelViewSet):
    queryset = FunctionalDisability.objects.all()
    serializer_class = FunctionalDisabilitySerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MalnutritionViewSet(CustomModelViewSet):
    queryset = Malnutrition.objects.all()
    serializer_class = MalnutritionSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CardiovascularFactorsViewSet(CustomModelViewSet):
    queryset = CardiovascularFactors.objects.all()
    serializer_class = CardiovascularFactorsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MisuseMedicationsViewSet(CustomModelViewSet):
    queryset = MisuseMedications.objects.all()
    serializer_class = MisuseMedicationsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SocialAspectsViewSet(CustomModelViewSet):
    queryset = SocialAspects.objects.all()
    serializer_class = SocialAspectsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class LowSocialSupportViewSet(CustomModelViewSet):
    queryset = LowSocialSupport.objects.all()
    serializer_class = LowSocialSupportSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class EnvironmentalProblemsViewSet(CustomModelViewSet):
    queryset = EnvironmentalProblems.objects.all()
    serializer_class = EnvironmentalProblemsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class ViolenceViewSet(CustomModelViewSet):
    queryset = Violence.objects.all()
    serializer_class = ViolenceSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


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
