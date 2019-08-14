from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from participant_section.api.serializers import ParticipantSerializer, IncomeSerializer, \
    ParticipantSocialMediaSerializer, MaritalStatusSerializer, SchoolingSerializer, ProfessionalsActivitiesSerializer, \
    ReligionSerializer, ParticipantSituationSerializer
from participant_section.models import Participant, Income, ParticipantSocialMedia, MaritalStatus, Schooling, \
    ProfessionalsActivities, Religion, ParticipantSituation


class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication', 'birth_date', 'gender')


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    # filter_backends = (SearchFilter,)
    # search_fields = ('range', )


class ParticipantSocialMediaViewSet(ModelViewSet):
    queryset = ParticipantSocialMedia.objects.all()
    serializer_class = ParticipantSocialMediaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class MaritalStatusViewSet(ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('status',)


class SchoolingViewSet(ModelViewSet):
    queryset = Schooling.objects.all()
    serializer_class = SchoolingSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('schooling',)


class ProfessionalsActivitiesViewSet(ModelViewSet):
    queryset = ProfessionalsActivities.objects.all()
    serializer_class = ProfessionalsActivitiesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class ReligionViewSet(ModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)


class ParticipantSituationViewSet(ModelViewSet):
    queryset = ParticipantSituation.objects.all()
    serializer_class = ParticipantSituationSerializer
    # filter_backends = (SearchFilter,)
    # search_fields = ('', )

