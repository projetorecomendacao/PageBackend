from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from institution_section.models import Cidade, Address, Locals, Professional, \
     Institution, AssistanceModality, WebAddress, Offers, Capacity, ExpertiseAreas, \
     AcademicEducation, TypeDigitalAddress, TypePhoneEmail, ActingTime, LongaDuracao, \
     Locals, Offers, WebAddress, WebAddressInstitution, WebAddressLocals, WebAddressProfessional, \
     PhoneInstitution, PhoneLocals, PhoneProfessional, Email, EmailInstitution, EmailLocals, \
     EmailProfessional
from institution_section.api.serializers import CidadeSerializer, AddressSerializer, \
     LocalsSerializer, ProfessionalSerializer, InstitutionSerializer, \
     AssistanceModalitySerializer, WebAddressSerializer, OffersSerializer, CapacitySerializer, \
     ExpertiseAreasSerializer, AcademicEducationSerializer, TypeDigitalAddressSerializer, \
     TypePhoneEmailSerializer, ActingTimeSerializer, LongaDuracaoSerializer, LocalsSerializer, \
     OffersSerializer, WebAddressSerializer, WebAddressInstitutionSerializer, \
     WebAddressLocalsSerializer, WebAddressProfessionalSerializer, \
     PhoneInstitutionSerializer, PhoneLocalsSerializer, PhoneProfessionalSerializer,\
     EmailSerializer, EmailInstitutionSerializer, EmailLocalsSerializer, EmailProfessionalSerializer
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


class AcademicEducationViewSet(ModelViewSet):
    queryset = AcademicEducation.objects.all()
    serializer_class = AcademicEducationSerializer


class TypeDigitalAddressViewSet(ModelViewSet):
    queryset = TypeDigitalAddress.objects.all()
    serializer_class = TypeDigitalAddressSerializer


class TypePhoneEmailViewSet(ModelViewSet):
    queryset = TypePhoneEmail.objects.all()
    serializer_class = TypePhoneEmailSerializer


class ActingTimeViewSet(ModelViewSet):
    queryset = ActingTime.objects.all()
    serializer_class = ActingTimeSerializer


class LongaDuracaoViewSet(ModelViewSet):
    queryset = LongaDuracao.objects.all()
    serializer_class = LongaDuracaoSerializer


class WebAddressViewSet(ModelViewSet):
    queryset = WebAddress.objects.all()
    serializer_class = WebAddressSerializer


class WebAddressInstitutionViewSet(ModelViewSet):
    queryset = WebAddressInstitution.objects.all()
    serializer_class = WebAddressInstitutionSerializer


class WebAddressLocalsViewSet(ModelViewSet):
    queryset = WebAddressLocals.objects.all()
    serializer_class = WebAddressLocalsSerializer


class WebAddressProfessionalViewSet(ModelViewSet):
    queryset = WebAddressProfessional.objects.all()
    serializer_class = WebAddressProfessionalSerializer


class PhoneInstitutionViewSet(ModelViewSet):
    queryset = PhoneInstitution.objects.all()
    serializer_class = PhoneInstitutionSerializer


class PhoneLocalsViewSet(ModelViewSet):
    queryset = PhoneLocals.objects.all()
    serializer_class = PhoneLocalsSerializer


class PhoneProfessionalViewSet(ModelViewSet):
    queryset = PhoneProfessional.objects.all()
    serializer_class = PhoneProfessionalSerializer


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class EmailInstitutionViewSet(ModelViewSet):
    queryset = EmailInstitution.objects.all()
    serializer_class = EmailInstitutionSerializer


class EmailLocalsViewSet(ModelViewSet):
    queryset = EmailLocals.objects.all()
    serializer_class = EmailLocalsSerializer


class EmailProfessionalViewSet(ModelViewSet):
    queryset = EmailProfessional.objects.all()
    serializer_class = EmailProfessionalSerializer

class ExpertiseAreasViewSet(ModelViewSet):
    queryset = ExpertiseAreas.objects.all()
    serializer_class = ExpertiseAreasSerializer
