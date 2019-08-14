from rest_framework.serializers import ModelSerializer
from participant_section.models import Participant, Income, ParticipantSocialMedia, MaritalStatus, Schooling, \
    ProfessionalsActivities, Religion, ParticipantSituation


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class ParticipantSocialMediaSerializer(ModelSerializer):
    class Meta:
        model = ParticipantSocialMedia
        fields = '__all__'


class MaritalStatusSerializer(ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'


class SchoolingSerializer(ModelSerializer):
    class Meta:
        model = Schooling
        fields = '__all__'


class ProfessionalsActivitiesSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalsActivities
        fields = '__all__'


class ReligionSerializer(ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'


class ParticipantSituationSerializer(ModelSerializer):
    class Meta:
        model = ParticipantSituation
        fields = '__all__'
        depth = 1
