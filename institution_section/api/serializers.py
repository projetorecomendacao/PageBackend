from rest_framework.serializers import ModelSerializer
from institution_section.models import Cidade, AddressPlace, Professional, \
     Institution, ActingArea, Offers, Capacity,  ExpertiseAreas, \
     AcademicEducation, WebAddressInstitution, PhoneInstitution, EmailInstitution, \
     LegalNature, PeopleType, PeopleSex, PeopleRangeAge, PeopleIncapacity,\
     TypeDigitalAddress

class TypeDigitalAddressSerializer(ModelSerializer):
    class Meta:
        model = TypeDigitalAddress
        fields = '__all__'

class ActingAreaSerializer(ModelSerializer):
    class Meta:
        model = ActingArea
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


class AddressPlaceSerializer(ModelSerializer):
    class Meta:
        model = AddressPlace
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


class WebAddressInstitutionSerializer(ModelSerializer):
    class Meta:
        model = WebAddressInstitution
        fields = '__all__'


class PhoneInstitutionSerializer(ModelSerializer):
    class Meta:
        model = PhoneInstitution
        fields = '__all__'


class EmailInstitutionSerializer(ModelSerializer):
    class Meta:
        model = EmailInstitution
        fields = '__all__'

class LegalNatureSerializer(ModelSerializer):
    class Meta:
        model = LegalNature
        fields = '__all__'

class PeopleTypeSerializer(ModelSerializer):
    class Meta:
        model = PeopleType
        fields = '__all__'

class PeopleSexSerializer(ModelSerializer):
    class Meta:
        model = PeopleSex 
        fields = '__all__'

class PeopleRangeAgeSerializer(ModelSerializer):
    class Meta:
        model = PeopleRangeAge
        fields = '__all__'

class PeopleIncapacitySerializer(ModelSerializer):
    class Meta:
        model = PeopleIncapacity
        fields = '__all__'