from rest_framework.response import Response
from django.forms.models import model_to_dict

from institution_section.models import Cidade, AddressPlace, Professional, \
     Institution, ActingArea, Offers, Capacity, ExpertiseAreas, \
     AcademicEducation, WebAddressInstitution, PhoneInstitution, \
     TargetAudience, EmailInstitution, \
     LegalNature, PeopleType, PeopleSex, PeopleRangeAge, PeopleIncapacity,\
     TypeDigitalAddress

from institution_section.api.serializers import CidadeSerializer, AddressPlaceSerializer, \
     ProfessionalSerializer, InstitutionSerializer, ActingAreaSerializer, OffersSerializer,\
     CapacitySerializer, ExpertiseAreasSerializer, AcademicEducationSerializer,  \
     WebAddressInstitutionSerializer, PhoneInstitutionSerializer, EmailInstitutionSerializer, \
     LegalNatureSerializer, PeopleTypeSerializer, PeopleSexSerializer, \
     PeopleRangeAgeSerializer, PeopleIncapacitySerializer, TypeDigitalAddressSerializer

from utils.api.serializer import CustomModelViewSet, IsExpert

class TypeDigitalAddressViewSet(CustomModelViewSet):
    queryset = TypeDigitalAddress.objects.all()
    serializer_class = TypeDigitalAddressSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    def list(self, request):
        volta = TypeDigitalAddress.objects.all()
        if not volta.exists():
            TypeDigitalAddress.objects.create(description = 'Twitter')
            TypeDigitalAddress.objects.create(description = 'LinkedIn')
            volta = TypeDigitalAddress.objects.all()            
        dados = TypeDigitalAddressSerializer(volta,many=True)
        return Response(dados.data)


class LegalNatureViewSet(CustomModelViewSet):
    queryset = LegalNature.objects.all()
    serializer_class = LegalNatureSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    def list(self, request):
        volta = LegalNature.objects.all()
        if not volta.exists():
            LegalNature.objects.create(description = 'Pública')
            LegalNature.objects.create(description = 'Privada')
            LegalNature.objects.create(description = 'Terceiro Setor')
            volta = LegalNature.objects.all()            
        dados = LegalNatureSerializer(volta,many=True)
        return Response(dados.data)

class PeopleTypeViewSet(CustomModelViewSet):
    queryset = PeopleType.objects.all()
    serializer_class = PeopleTypeSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    def list(self, request):
        volta = PeopleType.objects.all()
        if not volta.exists():
            r1 = PeopleType.objects.create(description = 'Adulto')
            r2 = PeopleType.objects.create(description = 'Idoso')
            r3 = PeopleType.objects.create(description = 'Criança')
            volta = PeopleType.objects.all()            
        dados = PeopleTypeSerializer(volta,many=True)
        return Response(dados.data)

class PeopleSexViewSet(CustomModelViewSet):
    queryset = PeopleSex.objects.all()
    serializer_class = PeopleSexSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    def list(self, request):
        volta = PeopleSex.objects.all()
        if not volta.exists():
            r1 = PeopleSex.objects.create(description = 'Homem')
            r2 = PeopleSex.objects.create(description = 'Mulher')
            r3 = PeopleSex.objects.create(description = 'Ambos')
            volta = PeopleSex.objects.all()            
        dados = PeopleSexSerializer(volta,many=True)
        return Response(dados.data)    


class PeopleRangeAgeViewSet(CustomModelViewSet):
    queryset = PeopleRangeAge.objects.all()
    serializer_class = PeopleRangeAgeSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    def list(self, request):
        volta = PeopleRangeAge.objects.all()
        if not volta.exists():
            r1 = PeopleRangeAge.objects.create(description = '20 a 29 anos')
            r2 = PeopleRangeAge.objects.create(description = '30 a 39 anos')
            r3 = PeopleRangeAge.objects.create(description = '40 a 49 anos')
            r4 = PeopleRangeAge.objects.create(description = '50 a 29 anos')
            r5 = PeopleRangeAge.objects.create(description = '60 a 39 anos')
            r6 = PeopleRangeAge.objects.create(description = '70 a 49 anos')
            r7 = PeopleRangeAge.objects.create(description = '80 a 29 anos')
            r8 = PeopleRangeAge.objects.create(description = '90 a 99 anos')
            r9 = PeopleRangeAge.objects.create(description = '100 a mais anos')
            volta = PeopleRangeAge.objects.all()            
        dados = PeopleRangeAgeSerializer(volta,many=True)
        return Response(dados.data)   
    

class PeopleIncapacityViewSet(CustomModelViewSet):
    queryset = PeopleIncapacity.objects.all()
    serializer_class = PeopleIncapacitySerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    def list(self, request):
        volta = PeopleIncapacity.objects.all()
        if not volta.exists():
            r1 = PeopleIncapacity.objects.create(description = 'Totalmente independente, não precisa de qualquer tipo de apoio na vida cotidiana')
            r2 = PeopleIncapacity.objects.create(description = 'Necessita de pequenos apoio na vida cotidiana e no apoio à mobilidade')
            r3 = PeopleIncapacity.objects.create(description = 'Necessita de apoio na higiene pessoal, tarefas de vida cotidiana e na mobilidade')
            r4 = PeopleIncapacity.objects.create(description = 'Totalmente dependente para a satisfação das necessidades básicas (alimentação,higiene, vestuário, mobilidade e etc)')
            volta = PeopleIncapacity.objects.all()            

        dados = PeopleIncapacitySerializer(volta,many=True)
        return Response(dados.data)    

class OffersViewSet(CustomModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

class CapacityViewSet(CustomModelViewSet):
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer


class CidadeViewSet(CustomModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [IsExpert]
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

class AddressPlaceViewSet(CustomModelViewSet):
    queryset = AddressPlace.objects.all()
    serializer_class = AddressPlaceSerializer


class ProfessionalViewSet(CustomModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }


class AcademicEducationViewSet(CustomModelViewSet):
    queryset = AcademicEducation.objects.all()
    serializer_class = AcademicEducationSerializer


class ActingAreaViewSet(CustomModelViewSet):
    queryset = ActingArea.objects.all()
    serializer_class = ActingAreaSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }
    

class WebAddressInstitutionViewSet(CustomModelViewSet):
    queryset = WebAddressInstitution.objects.all()
    serializer_class = WebAddressInstitutionSerializer

class PhoneInstitutionViewSet(CustomModelViewSet):
    queryset = PhoneInstitution.objects.all()
    serializer_class = PhoneInstitutionSerializer


class EmailInstitutionViewSet(CustomModelViewSet):
    queryset = EmailInstitution.objects.all()
    serializer_class = EmailInstitutionSerializer


class ExpertiseAreasViewSet(CustomModelViewSet):
    queryset = ExpertiseAreas.objects.all()
    serializer_class = ExpertiseAreasSerializer


class InstitutionViewSet(CustomModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }

    ##o método atribui auxilia no preenchimento dos valores dos objetos no create e no update
    def atribui (self, model_, json_):
        for attr, value in json_.items():
            try:
                setattr(model_, attr, value)  
            except:
                pass

    ## Método de criação de um novo Instituto
    def create(self,request, *args, **kwargs):
        ## Cria o objeto Institution
        institution_ = Institution()

        ## Cria e atribui o endereço
        address_ = AddressPlace()
        self.atribui(address_,request.data['addressPlace'])
        if not request.data['addressPlace']['cidade'] == '':
            cidade_ = Cidade.objects.get(pk=request.data['addressPlace']['cidade'])
            address_.cidade = cidade_
        address_.haveParking = request.data['addressPlace']['haveParking'] == 'true'
        address_.save()
        institution_.addressPlace = address_

        ## Cria e atribui o Longa Duração
        capacity_ = Capacity()
        self.atribui(capacity_,request.data['capacity'])
        capacity_.save()
        institution_.capacity = capacity_

        ## Cria e atribui O público alvo
        targetAudience_ = TargetAudience()
        targetAudience_.most_people_served_type = PeopleType.objects.get(pk=request.data['targetAudience']['most_people_served_type'])
        targetAudience_.people_can_be_served = PeopleType.objects.get(pk=request.data['targetAudience']['people_can_be_served'])
        targetAudience_.most_people_served_sex = PeopleSex.objects.get(pk=request.data['targetAudience']['most_people_served_sex'])
        targetAudience_.most_people_served_range_age = PeopleRangeAge.objects.get(pk=request.data['targetAudience']['most_people_served_range_age'])
        targetAudience_.most_people_served_incapacity = PeopleIncapacity.objects.get(pk=request.data['targetAudience']['most_people_served_incapacity'])
        targetAudience_.comments = request.data['targetAudience']['comments']
        targetAudience_.save()
        institution_.targetAudience = targetAudience_

        ## Atribui a chave primária da Área de Atuação
        mainActingArea_ = ActingArea.objects.get(pk=request.data['mainActingArea'])
        institution_.mainActingArea = mainActingArea_

        ##Este campo está desativado no frontend
        ## Atribui a chave primária ao Responsável Técnico
        ##professional_ = Professional.objects.get(pk=request.data['technicalResponsible'])
        ##institution_.technicalResponsible = professional_

        ## Atribui os campos simples do model
        institution_.company_name = request.data['company_name']
        institution_.trading_name = request.data['trading_name']
        institution_.trading_name_know = request.data['trading_name_know'] 
        institution_.cnpj = request.data['cnpj'] 
        institution_.category = request.data['category'] 
        institution_.foundation_year = request.data['foundation_year'] 
        institution_.legal_nature = request.data['legal_nature'] 
        institution_.objective = request.data['objective'] 
        institution_.schedules = request.data['schedules'] 
        institution_.phoneMain = request.data['phoneMain'] 
        institution_.phoneWhatsapp = request.data['phoneWhatsapp'] 
        institution_.emailMain = request.data['emailMain'] 
        institution_.facebook = request.data['facebook'] 
        institution_.instagram = request.data['instagram'] 
        institution_.webPage = request.data['webPage'] 

        ## Salva o objeto antes de povoar os relacionamentos
        institution_.save()

        ##Guarda a lista de telefones
        phoneList_ = request.data['phoneList']
        for phone_ in phoneList_:
            phone_inst = PhoneInstitution(description=phone_['description'],phone_number=phone_['phone_number'],institution=institution_)
            phone_inst.save()

        ##Guarda a lista de Emails
        emailList_ = request.data['emailList']
        for email_ in emailList_:
            email_inst = EmailInstitution(description=email_['description'],email_address=email_['email_address'],institution=institution_)
            email_inst.save()

        ##Guarda a lista de Endereços WEB
        webAddressList_ = request.data['webAddressList']
        for web_ in webAddressList_:
            typeDigitalAddress = TypeDigitalAddress.objects.get(pk=web_['description'])
            web_inst = WebAddressInstitution(description=typeDigitalAddress,digital_address=web_['digital_address'],institution=institution_)
            web_inst.save()

        ##Retorna o objeto
        return Response({'id': institution_.pk})

    ## Monta e retorna do objeto Institution
    def retrieve(self, request, pk=None):
        inst_ = Institution.objects.get(pk=pk)
        address_ = model_to_dict(AddressPlace.objects.get(pk=inst_.addressPlace.pk))
        capacity_ = model_to_dict(Capacity.objects.get(pk=inst_.capacity.pk))
        phoneList_ = list(PhoneInstitution.objects.filter(institution=inst_).values())
        emailList_ = list(EmailInstitution.objects.filter(institution=inst_).values())
        webAddressList_ = list(WebAddressInstitution.objects.filter(institution=inst_).values())
        targetAudience_ = model_to_dict(TargetAudience.objects.get(pk=inst_.targetAudience.pk))
        institution = InstitutionSerializer(inst_).data
        institution['targetAudience'] = targetAudience_
        institution['addressPlace'] = address_
        institution['phoneList'] = phoneList_ 
        institution['emailList'] = emailList_ 
        institution['webAddressList'] = webAddressList_
        institution['capacity'] = capacity_
        return Response(institution)

        
    def update(self, request, pk=None):
        ## Cria o objeto Institution
        institution_ = Institution.objects.get(pk=pk)


        ## Encontra e atribui os campos do endereço
        address_ = AddressPlace.objects.get(pk=institution_.addressPlace.pk)
        self.atribui(address_,request.data['addressPlace'])
        cidade_ = Cidade.objects.get(pk=request.data['addressPlace']['cidade'])
        address_.cidade = cidade_
        address_.haveParking = request.data['addressPlace']['haveParking'] == 'true'
        address_.save()

        ## Cria e atribui o Longa Duração
        capacity_ = Capacity.objects.get(pk=institution_.capacity.pk)
        self.atribui(capacity_,request.data['capacity'])
        capacity_.save()

        ## Cria e atribui o público alvo
        targetAudience_ = TargetAudience.objects.get(pk=institution_.targetAudience.pk)
        targetAudience_.most_people_served_type = PeopleType.objects.get(pk=request.data['targetAudience']['most_people_served_type'])
        targetAudience_.people_can_be_served = PeopleType.objects.get(pk=request.data['targetAudience']['people_can_be_served'])
        targetAudience_.most_people_served_sex = PeopleSex.objects.get(pk=request.data['targetAudience']['most_people_served_sex'])
        targetAudience_.most_people_served_range_age = PeopleRangeAge.objects.get(pk=request.data['targetAudience']['most_people_served_range_age'])
        targetAudience_.most_people_served_incapacity = PeopleIncapacity.objects.get(pk=request.data['targetAudience']['most_people_served_incapacity'])
        targetAudience_.comments = request.data['targetAudience']['comments']
        targetAudience_.save()

        ## Atribui a chave primária da Área de Atuação
        mainActingArea_ = ActingArea.objects.get(pk=request.data['mainActingArea'])
        institution_.mainActingArea = mainActingArea_

        #Desligado no frontend
        ## Atribui a chave primária ao Responsável Técnico
        #professional_ = Professional.objects.get(pk=request.data['technicalResponsible'])
        #institution_.technicalResponsible = professional_

        ## Atribui os campos simples do model
        institution_.company_name = request.data['company_name']
        institution_.trading_name = request.data['trading_name']
        institution_.trading_name_know = request.data['trading_name_know'] 
        institution_.cnpj = request.data['cnpj'] 
        institution_.category = request.data['category'] 
        institution_.foundation_year = request.data['foundation_year'] 
        institution_.legal_nature = request.data['legal_nature'] 
        institution_.objective = request.data['objective'] 
        institution_.schedules = request.data['schedules'] 
        institution_.phoneMain = request.data['phoneMain'] 
        institution_.phoneWhatsapp = request.data['phoneWhatsapp'] 
        institution_.emailMain = request.data['emailMain'] 
        institution_.facebook = request.data['facebook'] 
        institution_.instagram = request.data['instagram'] 
        institution_.webPage = request.data['webPage'] 


        ## Salva o objeto antes de povoar os relacionamentos
        institution_.save()

        ##Guarda a lista de telefones
        #Apaga todos os existentes
        delPhone = PhoneInstitution.objects.filter(institution=institution_).delete()
        #Cria tudo de novo com o que veio do form
        phoneList_ = request.data['phoneList']
        for phone_ in phoneList_:
            phone_inst = PhoneInstitution(description=phone_['description'],phone_number=phone_['phone_number'],institution=institution_)
            phone_inst.save()

        ##Guarda a lista de Emails
        #Apaga a lista de email
        delEmail = EmailInstitution.objects.filter(institution=institution_).delete()
        #Cria a lista de novo com o que veio do form
        emailList_ = request.data['emailList']
        for email_ in emailList_:
            email_inst = EmailInstitution(description=email_['description'],email_address=email_['email_address'],institution=institution_)
            email_inst.save()

        ##Guarda a lista de Endereços WEB
        #apaga a lista de endereços WEB
        delWeb = WebAddressInstitution.objects.filter(institution=institution_).delete()
        #cria lista de novo
        ##Guarda a lista de Endereços WEB
        webAddressList_ = request.data['webAddressList']
        for web_ in webAddressList_:
            typeDigitalAddress = TypeDigitalAddress.objects.get(pk=web_['description'])
            web_inst = WebAddressInstitution(description=typeDigitalAddress,digital_address=web_['digital_address'],institution=institution_)
            web_inst.save()

        ##Retorna o objeto
        return Response({'id': institution_.pk})        
