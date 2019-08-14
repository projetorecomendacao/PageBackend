from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from institution_section.models import Address, Contact, Location, Professional, Instructor, Responsible, Institution
from institution_section.api.serializers import AddressSerializer, ContactSerializer, LocationSerializer,\
    ProfessionalSerializer, InstructorSerializer, ResponsibleSerializer, InstitutionSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('address', 'district', 'cep')


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # filter_backends = (SearchFilter,)
    # search_fields = ('description',)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication', 'parking')


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication', 'parking')


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication', 'formation')


class ResponsibleViewSet(ModelViewSet):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication')  # , 'area')


class InstitutionViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'communication')
