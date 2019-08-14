from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from activities_section.models import Characteristic, Benefit, Restriction, Type, Activity
from activities_section.api.serializers import CharacteristicSerializer, BenefitSerializer,\
    RestrictionSerializer, TypeSerializer, ActivitySerializer


class CharacteristicViewSet(ModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class BenefitViewSet(ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class RestrictionViewSet(ModelViewSet):
    queryset = Restriction.objects.all()
    serializer_class = RestrictionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
