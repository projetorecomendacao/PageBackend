from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from assessment_section.models import *
from assessment_section.api.serializers import *
from utils.api.serializer import CustomModelViewSet, IsExpert

class DemandsProblemsViewSet(CustomModelViewSet):
    queryset = DemandsProblems.objects.all()
    serializer_class = DemandsProblemsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class ActionsViewSet(CustomModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class ServicesViewSet(CustomModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class GoalsViewSet(CustomModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class ActionsPlanningViewSet(CustomModelViewSet):
    queryset = ActionsPlanning.objects.all()
    serializer_class = ActionsPlanningSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('')


class ActionsImplementationCoordenationViewSet(CustomModelViewSet):
    queryset = ActionImplementationCoordenation.objects.all()
    serializer_class = ActionImplementationCoordenationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('data')

class ReassessmentControlViewSet(CustomModelViewSet):
    queryset = ReassessmentControl .objects.all()
    serializer_class = ReassessmentControlSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('data')  # , 'area')

class DemandMapViewSet(CustomModelViewSet):
    queryset = DemandMap.objects.all()
    serializer_class = DemandMapSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('created_at')  # , 'area')
