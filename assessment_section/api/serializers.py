from rest_framework.serializers import ModelSerializer
from assessment_section.models import *

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

class ActionsPlanningSerializer (ModelSerializer):
    class Meta:
        model = ActionsPlanning
        fields = '__all__'

class ActionImplementationCoordenationSerializer (ModelSerializer):
    class Meta:
        model = ActionImplementationCoordenation
        fields = '__all__'

class ReassessmentControlSerializer(ModelSerializer):
    class Meta:
        model = ReassessmentControl
        fields = '__all__'

class DemandMapSerializer(ModelSerializer):
    class Meta:
        model = DemandMap
        fields = '__all__'



