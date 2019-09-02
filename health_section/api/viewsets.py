from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from health_section.models import Diseases, TherapeuticClass, HealthProblems, Medicines, Fractures
from health_section.api.serializers import DiseasesSerializer, TherapeuticClassSerializer, HealthProblemsSerializer, MedicinesSerializer, FracturesSerializer

class DiseasesViewSet(ModelViewSet):
    queryset = Diseases.objects.all()
    serializer_class = DiseasesSerializer

class TherapeuticClassViewSet(ModelViewSet):
    queryset = TherapeuticClass.objects.all()
    serializer_class = TherapeuticClassSerializer

class HealthProblemsViewSet(ModelViewSet):
    queryset = HealthProblems.objects.all()
    serializer_class = HealthProblemsSerializer

class MedicinesViewSet(ModelViewSet):
    queryset = Medicines.objects.all()
    serializer_class = MedicinesSerializer

class FracturesViewSet(ModelViewSet):
    queryset = Fractures.objects.all()
    serializer_class = FracturesSerializer
