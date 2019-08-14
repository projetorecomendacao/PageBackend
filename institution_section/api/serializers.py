from rest_framework.serializers import ModelSerializer
from institution_section.models import Address, Contact, Location, Professional, Instructor, Responsible, Institution


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        # all address attributes plus location and institution that are linked to address through an one to one
        # relation.
        fields = '__all__'
        # fields = ('address', 'number', 'district', 'cep', 'latitude', 'longitude', 'locations', 'institution')


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProfessionalSerializer(ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'


class InstructorSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class ResponsibleSerializer(ModelSerializer):
    class Meta:
        model = Responsible
        fields = '__all__'


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        # all institution attributes plus contacts and locations that are linked to institution through an one to one
        # relation.
        fields = '__all__'
        # fields = ('name', 'communication', 'address', 'contacts', 'locations')
