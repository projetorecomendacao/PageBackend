from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from experts_section.models import Expert
from participant_section.api.serializers import ParticipantSerializer, IncomeSerializer, \
    ParticipantSocialMediaSerializer, MaritalStatusSerializer, SchoolingSerializer, ProfessionalsActivitiesSerializer, \
    ReligionSerializer, ParticipantSituationSerializer
from participant_section.models import Participant, Income, ParticipantSocialMedia, MaritalStatus, Schooling, \
    ProfessionalsActivities, Religion, ParticipantSituation
from utils.api.serializer import IsExpert, CustomModelViewSet


class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication', 'birth_date', 'gender')
    permission_classes = [IsExpert]

    def get_queryset(self):
        return Expert.objects.get(email=self.request.user.email).contacts

    def create(self, request, *args, **kwargs):
        participant = Participant.objects.filter(p00_email=self.request.data.get('p00_email'))
        if participant.exists():
            participant = participant.first()
            Expert.objects.get(email=self.request.user.email).contacts.add(participant)
            serializer = self.get_serializer(participant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return super().create(request, args, kwargs)

    def perform_create(self, serializer):
        Expert.objects.get(email=self.request.user.email).contacts.add(serializer.save())

    def destroy(self, request, *args, **kwargs):
        Expert.objects.get(email=self.request.user.email).contacts.remove(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ParticipantSituationViewSet(CustomModelViewSet):
    queryset = ParticipantSituation.objects.all()
    serializer_class = ParticipantSituationSerializer
    # filter_backends = (SearchFilter,)
    # search_fields = ('', )
    permission_classes_by_action = {
        'create': [IsAuthenticated]
    }

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

