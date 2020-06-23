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


class NegativeAttitudesAgingViewSet(CustomModelViewSet):
    queryset = NegativeAttitudesAgingUsp.objects.all()
    Serializer_class = NegativeAttitudesAgingUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CognitionDeficitViewSet(CustomModelViewSet):
    queryset = CognitionDeficitUsp.objects.all()
    Serializer_class = CognitionDeficitUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class DepressionViewSet(CustomModelViewSet):
    queryset = DepressionUsp.objects.all()
    Serializer_class = DepressionUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PsychologicalAspectsViewSet(CustomModelViewSet):
    queryset = PsychologicalAspectsUsp.objects.all()
    Serializer_class = PsychologicalAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class BiologicalAspectsViewSet(CustomModelViewSet):
    queryset = BiologicalAspectsUsp.objects.all()
    Serializer_class = BiologicalAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SensoryDeficitViewSet(CustomModelViewSet):
    queryset = SensoryDeficitUsp.objects.all()
    Serializer_class = SensoryDeficitUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FunctionalDisabilityViewSet(CustomModelViewSet):
    queryset = FunctionalDisabilityUsp.objects.all()
    Serializer_class = FunctionalDisabilityUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MalnutritionViewSet(CustomModelViewSet):
    queryset = MalnutritionUsp.objects.all()
    Serializer_class = MalnutritionUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CardiovascularFactorsViewSet(CustomModelViewSet):
    queryset = CardiovascularFactorsUsp.objects.all()
    Serializer_class = CardiovascularFactorsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MisuseMedicationsViewSet(CustomModelViewSet):
    queryset = MisuseMedicationsUsp.objects.all()
    Serializer_class = MisuseMedicationsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SocialAspectsViewSet(CustomModelViewSet):
    queryset = SocialAspectsUsp.objects.all()
    Serializer_class = SocialAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class LowSocialSupportViewSet(CustomModelViewSet):
    queryset = LowSocialSupportUsp.objects.all()
    Serializer_class = LowSocialSupportUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class EnvironmentalProblemsViewSet(CustomModelViewSet):
    queryset = EnvironmentalProblemsUsp.objects.all()
    Serializer_class = EnvironmentalProblemsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class ViolenceViewSet(CustomModelViewSet):
    queryset = ViolenceUsp.objects.all()
    Serializer_class = ViolenceUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MultidisciplinaryDomainViewSet(CustomModelViewSet):
    queryset = MultidisciplinaryDomainUsp.objects.all()
    Serializer_class = MultidisciplinaryDomainUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FallsViewSet(CustomModelViewSet):
    queryset = FallsUsp.objects.all()
    Serializer_class = FallsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PageViewSet (CustomModelViewSet):
    queryset = PageUsp.objects.all()
    Serializer_class = PageUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }