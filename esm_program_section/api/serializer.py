from rest_framework.serializers import ModelSerializer

from esm_program_section.models import Program, Intervention, ActiveEvent, ActionsEsm, EditorProgram

class EditorProgramSerializer (ModelSerializer):
    class Meta:
        model = EditorProgram
        fields = '__all__'

class ProgramSerializer (ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class ActiveEventSerializer (ModelSerializer):
    class Meta:
        model = ActiveEvent
        fields = '__all__'

class InterventionSerializer (ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'

class ActionsEsmSerializer (ModelSerializer):
    class Meta:
        model = ActionsEsm
        fields = '__all__'
