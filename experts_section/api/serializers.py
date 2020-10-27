from rest_framework.serializers import ModelSerializer
from experts_section.models import Expert, Expertise, Orientador


class ExpertSerializer(ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'


class ExpertiseSerializer(ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'


class OrientadorSerializer(ModelSerializer):
    class Meta:
        model = Orientador
        fields = '__all__'
