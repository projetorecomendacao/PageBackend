from rest_framework.serializers import ModelSerializer
from institution_section.models import Cidade, Address, Locals, Professional, \
     Institution, AssistanceModality, WebAddress, Offers, Capacity,  ExpertiseAreas, \
     AcademicEducation, TypeDigitalAddress, TypePhoneEmail, ActingTime, LongaDuracao, \
     Locals, Offers, WebAddress, WebAddressInstitution, WebAddressLocals, WebAddressProfessional, \
     PhoneInstitution, PhoneLocals, PhoneProfessional, Email, EmailInstitution, EmailLocals, \
     EmailProfessional

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

class ExpertiseAreasSerializer(ModelSerializer):
    class Meta:
        model = ExpertiseAreas
        fields = '__all__'


class AcademicEducationSerializer(ModelSerializer):
    class Meta:
        model = AcademicEducation
        fields = '__all__'


class TypeDigitalAddressSerializer(ModelSerializer):
    class Meta:
        model = TypeDigitalAddress
        fields = '__all__'


class TypePhoneEmailSerializer(ModelSerializer):
    class Meta:
        model = TypePhoneEmail
        fields = '__all__'


class ActingTimeSerializer(ModelSerializer):
    class Meta:
        model = ActingTime
        fields = '__all__'


class LongaDuracaoSerializer(ModelSerializer):
    class Meta:
        model = LongaDuracao
        fields = '__all__'


class WebAddressSerializer(ModelSerializer):
    class Meta:
        model = WebAddress
        fields = '__all__'


class WebAddressInstitutionSerializer(ModelSerializer):
    class Meta:
        model = WebAddressInstitution
        fields = '__all__'


class WebAddressLocalsSerializer(ModelSerializer):
    class Meta:
        model = WebAddressLocals
        fields = '__all__'


class WebAddressProfessionalSerializer(ModelSerializer):
    class Meta:
        model = WebAddressProfessional
        fields = '__all__'


class PhoneInstitutionSerializer(ModelSerializer):
    class Meta:
        model = PhoneInstitution
        fields = '__all__'


class PhoneLocalsSerializer(ModelSerializer):
    class Meta:
        model = PhoneLocals
        fields = '__all__'


class PhoneProfessionalSerializer(ModelSerializer):
    class Meta:
        model = PhoneProfessional
        fields = '__all__'


class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email 
        fields = '__all__'


class EmailInstitutionSerializer(ModelSerializer):
    class Meta:
        model = EmailInstitution
        fields = '__all__'


class EmailLocalsSerializer(ModelSerializer):
    class Meta:
        model = EmailLocals
        fields = '__all__'


class EmailProfessionalSerializer(ModelSerializer):
    class Meta:
        model = EmailProfessional
        fields = '__all__'


