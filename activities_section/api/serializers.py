from rest_framework.serializers import ModelSerializer
from activities_section.models import Characteristic, Benefit, Restriction, Type, Activity


class CharacteristicSerializer(ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class BenefitSerializer(ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'


class RestrictionSerializer(ModelSerializer):
    class Meta:
        model = Restriction
        fields = '__all__'


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        depth = 1
