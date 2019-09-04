from rest_framework.serializers import ModelSerializer
from health_section.models import Diseases, TherapeuticClass, HealthProblems, Medicines, Fractures

class DiseasesSerializer(ModelSerializer):
    class Meta:
        model = Diseases
        fields = '__all__'

class TherapeuticClassSerializer(ModelSerializer):
    class Meta:
        model = TherapeuticClass
        fields = '__all__'


class HealthProblemsSerializer(ModelSerializer):
    class Meta:
        model = HealthProblems
        fields = '__all__'


class MedicinesSerializer(ModelSerializer):
    class Meta:
        model = Medicines
        fields = '__all__'


class FracturesSerializer(ModelSerializer):
    class Meta:
        model = Fractures
        fields = '__all__'
