from rest_framework.serializers import ModelSerializer
from experts_section.models import Expert, Expertise


class ExpertSerializer(ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'


class ExpertiseSerializer(ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'
