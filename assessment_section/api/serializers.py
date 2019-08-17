from rest_framework.serializers import ModelSerializer
from assessment_section.models import DemandsProblems, Actions, Services, Goals, AssessmentsControl, ExpertAssessment, ActionsImplementation


class DemandsProblemsSerializer(ModelSerializer):
    class Meta:
        model = DemandsProblems
        fields = '__all__'


class ActionsSerializer(ModelSerializer):
    class Meta:
        model = Actions,
        fields = '__all__'


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class GoalsSerializer(ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class AssessmentControlSerializer(ModelSerializer):
    class Meta:
        model = AssessmentsControl
        fields = '__all__'


class ExpertAssessmentSerializer(ModelSerializer):
    class Meta:
        model = ExpertAssessment
        fields = '__all__'


class ActionImplementationSerializer(ModelSerializer):
    class Meta:
        model = ActionsImplementation
        fields = '__all__'

