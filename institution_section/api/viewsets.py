from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from institution_section.models import Cidade, Address, Locals, Professional, \
     Institution, AssistanceModality, WebAddress, Offers, Capacity
from institution_section.api.serializers import CidadeSerializer, AddressSerializer, \
     LocalsSerializer, ProfessionalSerializer, InstitutionSerializer, \
     AssistanceModalitySerializer, WebAddressSerializer, OffersSerializer, CapacitySerializer
from utils.api.serializer import CustomModelViewSet, IsExpert

class AssistanceModalityViewSet(ModelViewSet):
    queryset = AssistanceModality.objects.all()
    serializer_class = AssistanceModalitySerializer


class WebAddressViewSet(ModelViewSet):
    queryset = WebAddress.objects.all()
    serializer_class = WebAddressSerializer


class OffersViewSet(ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer


class CapacityViewSet(ModelViewSet):
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [IsExpert]


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class LocalsViewSet(ModelViewSet):
    queryset = Locals.objects.all()
    serializer_class = LocalsSerializer


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class InstitutionViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

