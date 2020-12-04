from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from health_section.models import Diseases, TherapeuticClass, HealthProblems, Medicines, Fractures
from health_section.api.serializers import DiseasesSerializer, TherapeuticClassSerializer, HealthProblemsSerializer, MedicinesSerializer, FracturesSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert

class DiseasesViewSet(CustomModelViewSet):
    queryset = Diseases.objects.all()
    serializer_class = DiseasesSerializer

class TherapeuticClassViewSet(CustomModelViewSet):
    queryset = TherapeuticClass.objects.all()
    serializer_class = TherapeuticClassSerializer

class HealthProblemsViewSet(CustomModelViewSet):
    queryset = HealthProblems.objects.all()
    serializer_class = HealthProblemsSerializer

class MedicinesViewSet(CustomModelViewSet):
    queryset = Medicines.objects.all()
    serializer_class = MedicinesSerializer

class FracturesViewSet(CustomModelViewSet):
    queryset = Fractures.objects.all()
    serializer_class = FracturesSerializer
