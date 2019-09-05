from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from page_section.models import NegativeAttitudesAging, CognitionDeficit, Depression, PsychologicalAspects, \
    BiologicalAspects, SensoryDeficit, FunctionalDisability, Malnutrition, CardiovascularFactors, MisuseMedications, \
    SocialAspects, LowSocialSupport, EnvironmentalProblems, Violence, MultidisciplinaryDomain, Falls, Page
from page_section.api.serializers import NegativeAttitudesAgingSerializer, CognitionDeficitSerializer,\
    DepressionSerializer, PsychologicalAspectsSerializer, BiologicalAspectsSerializer, SensoryDeficitSerializer,\
    FunctionalDisabilitySerializer, MalnutritionSerializer, CardiovascularFactorsSerializer,\
    MisuseMedicationsSerializer, SocialAspectsSerializer, LowSocialSupportSerializer, EnvironmentalProblemsSerializer,\
    ViolenceSerializer, MultidisciplinaryDomainSerializer, FallsSerializer, PageSerializer


class NegativeAttitudesAgingViewSet(ModelViewSet):
    queryset = NegativeAttitudesAging.objects.all()
    serializer_class = NegativeAttitudesAgingSerializer


class CognitionDeficitViewSet(ModelViewSet):
    queryset = CognitionDeficit.objects.all()
    serializer_class = CognitionDeficitSerializer


class DepressionViewSet(ModelViewSet):
    queryset = Depression.objects.all()
    serializer_class = DepressionSerializer


class PsychologicalAspectsViewSet(ModelViewSet):
    queryset = PsychologicalAspects.objects.all()
    serializer_class = PsychologicalAspectsSerializer


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
