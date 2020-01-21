from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from activities_section.models import Characteristic, Benefit, Restriction, Type, Activity
from activities_section.api.serializers import CharacteristicSerializer, BenefitSerializer,\
    RestrictionSerializer, TypeSerializer, ActivitySerializer
from utils.api.serializer import CustomModelViewSet, IsExpert


class CharacteristicViewSet(CustomModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert]
    }


class BenefitViewSet(CustomModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert]
    }


class RestrictionViewSet(CustomModelViewSet):
    queryset = Restriction.objects.all()
    serializer_class = RestrictionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert]
    }


class TypeViewSet(CustomModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert]
    }


class ActivityViewSet(CustomModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert]
    }
    depth = 1
