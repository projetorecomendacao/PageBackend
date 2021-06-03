from rest_framework.serializers import ModelSerializer

from editor_psicometrico.models import Documento

class DocumentoSerializer (ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'
