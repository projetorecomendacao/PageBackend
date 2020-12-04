from rest_framework.filters import SearchFilter
from activities_section.models import Characteristic, Benefit, Restriction, Type, Activity
from activities_section.api.serializers import CharacteristicSerializer, BenefitSerializer,\
    RestrictionSerializer, TypeSerializer, ActivitySerializer
from utils.api.serializer import CustomModelViewSet, IsExpert
from rest_framework.response import Response


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
        'destroy': [IsExpert],
        'update': [IsExpert]
    }
    depth = 1

    def update(self, request, pk=None):
        instance = Activity.objects.get(pk=pk)
        instance.type_activity.clear()
        instance.benefit.clear()
        instance.restriction.clear()
        instance.characteristic.clear()

        instance.title = request.data['title']
        instance.description = request.data['description']
        instance.imageURL = request.data['imageURL']
        instance.general_activity_objective = request.data['general_activity_objective']
        instance.author = request.data['author']

        instance.save()


        for id in request.data['characteristic']:
            chara_ = Characteristic.objects.get(id=id['id'])
            try:
                instance.characteristic.add(chara_)
            except:
                pass

        for id in request.data['benefit']:
            bene_ = Benefit.objects.get(id=id['id'])
            try:
                instance.benefit.add(bene_)
            except:
                pass

        for id in request.data['restriction']:
            rest_ = Restriction.objects.get(id=id['id'])
            try:
                instance.restriction.add(rest_)
            except:
                pass

        for id in request.data['type_activity']:
            type_ = Type.objects.get(id=id['id'])
            try:
                instance.type_activity.add(type_)
            except:
                pass
        
        return Response ({'id' : instance.pk})

    def create(self, request, *args, **kwargs):
        instance = Activity()

        instance.title = request.data['title']
        instance.description = request.data['description']
        instance.imageURL = request.data['imageURL']
        instance.general_activity_objective = request.data['general_activity_objective']
        instance.author = request.data['author']

        instance.save()


        for id in request.data['characteristic']:
            chara_ = Characteristic.objects.get(id=id['id'])
            try:
                instance.characteristic.add(chara_)
            except:
                pass

        for id in request.data['benefit']:
            bene_ = Benefit.objects.get(id=id['id'])
            try:
                instance.benefit.add(bene_)
            except:
                pass

        for id in request.data['restriction']:
            rest_ = Restriction.objects.get(id=id['id'])
            try:
                instance.restriction.add(rest_)
            except:
                pass

        for id in request.data['type_activity']:
            type_ = Type.objects.get(id=id['id'])
            try:
                instance.type_activity.add(type_)
            except:
                pass
        
        return Response ({'id' : instance.pk})            

