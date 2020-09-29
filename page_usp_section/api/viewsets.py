from rest_framework.response import Response
from rest_framework import status

from experts_section.models import Expert
from page_usp_section.models_1_psicologico_usp import NegativeAttitudesAgingUsp, CognitionDeficitUsp, DepressionUsp, PsychologicalAspectsUsp
from page_usp_section.models_2_Biologicos_usp import BiologicalAspectsUsp, SensoryDeficitUsp, FunctionalDisabilityUsp, MalnutritionUsp, CardiovascularFactorsUsp, MisuseMedicationsUsp
from page_usp_section.models_3_sociais_usp import SocialAspectsUsp, LowSocialSupportUsp, EnvironmentalProblemsUsp, ViolenceUsp
from page_usp_section.models_4_multidimensional_usp import MultidisciplinaryDomainUsp, FallsUsp
from page_usp_section.models_0_page_usp import PageUsp
from page_usp_section.api.serializers import NegativeAttitudesAgingUspSerializer, CognitionDeficitUspSerializer,\
    DepressionUspSerializer, PsychologicalAspectsUspSerializer, BiologicalAspectsUspSerializer, SensoryDeficitUspSerializer,\
    FunctionalDisabilityUspSerializer, MalnutritionUspSerializer, CardiovascularFactorsUspSerializer,\
    MisuseMedicationsUspSerializer, SocialAspectsUspSerializer, LowSocialSupportUspSerializer, EnvironmentalProblemsUspSerializer,\
    ViolenceUspSerializer, MultidisciplinaryDomainUspSerializer, FallsUspSerializer, PageUspSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert


class NegativeAttitudesAgingViewSetUsp(CustomModelViewSet):
    queryset = NegativeAttitudesAgingUsp.objects.all()
    serializer_class = NegativeAttitudesAgingUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CognitionDeficitViewSetUsp(CustomModelViewSet):
    queryset = CognitionDeficitUsp.objects.all()
    serializer_class = CognitionDeficitUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class DepressionViewSetUsp(CustomModelViewSet):
    queryset = DepressionUsp.objects.all()
    serializer_class = DepressionUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PsychologicalAspectsViewSetUsp(CustomModelViewSet):
    queryset = PsychologicalAspectsUsp.objects.all()
    serializer_class = PsychologicalAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class BiologicalAspectsViewSetUsp(CustomModelViewSet):
    queryset = BiologicalAspectsUsp.objects.all()
    serializer_class = BiologicalAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SensoryDeficitViewSetUsp(CustomModelViewSet):
    queryset = SensoryDeficitUsp.objects.all()
    serializer_class = SensoryDeficitUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FunctionalDisabilityViewSetUsp(CustomModelViewSet):
    queryset = FunctionalDisabilityUsp.objects.all()
    serializer_class = FunctionalDisabilityUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MalnutritionViewSetUsp(CustomModelViewSet):
    queryset = MalnutritionUsp.objects.all()
    serializer_class = MalnutritionUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CardiovascularFactorsViewSetUsp(CustomModelViewSet):
    queryset = CardiovascularFactorsUsp.objects.all()
    serializer_class = CardiovascularFactorsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MisuseMedicationsViewSetUsp(CustomModelViewSet):
    queryset = MisuseMedicationsUsp.objects.all()
    serializer_class = MisuseMedicationsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SocialAspectsViewSetUsp(CustomModelViewSet):
    queryset = SocialAspectsUsp.objects.all()
    serializer_class = SocialAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class LowSocialSupportViewSetUsp(CustomModelViewSet):
    queryset = LowSocialSupportUsp.objects.all()
    serializer_class = LowSocialSupportUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class EnvironmentalProblemsViewSetUsp(CustomModelViewSet):
    queryset = EnvironmentalProblemsUsp.objects.all()
    serializer_class = EnvironmentalProblemsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class ViolenceViewSetUsp(CustomModelViewSet):
    queryset = ViolenceUsp.objects.all()
    serializer_class = ViolenceUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MultidisciplinaryDomainViewSetUsp(CustomModelViewSet):
    queryset = MultidisciplinaryDomainUsp.objects.all()
    serializer_class = MultidisciplinaryDomainUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FallsViewSetUsp(CustomModelViewSet):
    queryset = FallsUsp.objects.all()
    serializer_class = FallsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PageViewSetUsp(CustomModelViewSet):
    queryset = PageUsp.objects.all()
    serializer_class = PageUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }