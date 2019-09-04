from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from assessment_section.models import DemandsProblems, Actions, Services, Goals, AssessmentsControl, ExpertAssessment, ActionsImplementation
from assessment_section.api.serializers import DemandsProblemsSerializer, ActionsSerializer, ServicesSerializer, GoalsSerializer, AssessmentControlSerializer, ExpertAssessmentSerializer, ActionImplementationSerializer

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


class AssessmentsControlViewSet(ModelViewSet):
    queryset = AssessmentsControl.objects.all()
    serializer_class = AssessmentControlSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('data', 'result', 'adequacy')


class ExpertAssessmentViewSet(ModelViewSet):
    queryset = ExpertAssessment.objects.all()
    serializer_class = ExpertAssessmentSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')  # , 'area')


class ActionsImplementationViewSet(ModelViewSet):
    queryset = ActionsImplementation.objects.all()
    serializer_class = ActionImplementationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('data')
