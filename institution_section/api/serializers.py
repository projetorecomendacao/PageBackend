from rest_framework.serializers import ModelSerializer
from institution_section.models import Cidade, Address, Locals, Professional, \
     Institution, AssistanceModality, WebAddress, Offers, Capacity

class AssistanceModalitySerializer(ModelSerializer):
    class Meta:
        model = AssistanceModality
        fields = '__all__'


class WebAddressSerializer(ModelSerializer):
    class Meta:
        model = WebAddress
        fields = '__all__'


class OffersSerializer(ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'


class CapacitySerializer(ModelSerializer):
    class Meta:
        model = Capacity
        fields = '__all__'


class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class LocalsSerializer(ModelSerializer):
    class Meta:
        model = Locals
        fields = '__all__'


class ProfessionalSerializer(ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

