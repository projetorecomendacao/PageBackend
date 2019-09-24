from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from assessment_section.models import *
from assessment_section.api.serializers import *

class DemandsProblemsViewSet(ModelViewSet):
    queryset = DemandsProblems.objects.all()
    serializer_class = DemandsProblemsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class ActionsViewSet(ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class GoalsViewSet(ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class ActionsPlanningViewSet(ModelViewSet):
    queryset = ActionsPlanning.objects.all()
    serializer_class = ActionsPlanningSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('')


class ActionsImplementationCoordenationViewSet(ModelViewSet):
    queryset = ActionImplementationCoordenation.objects.all()
    serializer_class = ActionImplementationCoordenationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('data')

class ReassessmentControlViewSet(ModelViewSet):
    queryset = ReassessmentControl .objects.all()
    serializer_class = ReassessmentControlSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('data')  # , 'area')

class DemandMapViewSet(ModelViewSet):
    queryset = DemandMap.objects.all()
    serializer_class = DemandMapSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('created_at')  # , 'area')
