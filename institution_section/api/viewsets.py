from rest_framework.response import Response
import json
from django.forms.models import model_to_dict

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from institution_section.models import Cidade, AddressPlace, Professional, \
     Institution, ActingArea, Offers, Capacity, ExpertiseAreas, \
     AcademicEducation, WebAddressInstitution, PhoneInstitution, \
     TargetAudience, EmailInstitution

from institution_section.api.serializers import CidadeSerializer, AddressPlaceSerializer, \
     ProfessionalSerializer, InstitutionSerializer, ActingAreaSerializer, OffersSerializer,\
     CapacitySerializer, ExpertiseAreasSerializer, AcademicEducationSerializer,  \
     WebAddressInstitutionSerializer, PhoneInstitutionSerializer, EmailInstitutionSerializer

from utils.api.serializer import CustomModelViewSet, IsExpert

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
        ## Cria o objeto Intitution
        institution_ = Institution()

        ## Cria e atribui o endereço
        address_ = AddressPlace()
        self.atribui(address_,request.data['addressPlace'])
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

        ## Cria e atribui o Longa Duração
        targetAudience_ = TargetAudience()
        self.atribui(targetAudience_,request.data['targetAudience'])
        targetAudience_.save()
        institution_.targetAudience = targetAudience_

        ## Atribui a chave primária da Área de Atuação
        mainActingArea_ = ActingArea.objects.get(pk=request.data['mainActingArea'])
        institution_.mainActingArea = mainActingArea_

        ## Atribui a chave primária ao Responsável Técnico
        professional_ = Professional.objects.get(pk=request.data['technicalResponsible'])
        institution_.technicalResponsible = professional_

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
            web_inst = WebAddressInstitution(description=web_['description'],digital_address=web_['digital_address'],institution=institution_)
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


        return Response({'id' : inst_.pk,
                        'company_name' : inst_.company_name,
                        'trading_name' : inst_.trading_name,
                        'trading_name_know' : inst_.trading_name_know,
                        'cnpj' : inst_.cnpj,
                        'category' : inst_.category,
                        'foundation_year' : inst_.foundation_year,
                        'legal_nature' : inst_.legal_nature,
                        'objective' : inst_.objective,
                        'schedules' : inst_.schedules,
                        'technicalResponsible' : inst_.technicalResponsible.pk,
                        'targetAudience' : targetAudience_,
                        'addressPlace': address_,
                        'phoneList' : phoneList_, 
                        'emailList' : emailList_, 
                        'webAddressList' : webAddressList_,
                        'capacity' : capacity_,
                        'mainActingArea' : inst_.mainActingArea.pk, 
                        })
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

        ## Cria e atribui o Longa Duração
        targetAudience_ = TargetAudience.objects.get(pk=institution_.targetAudience.pk)
        self.atribui(targetAudience_,request.data['targetAudience'])
        targetAudience_.save()

        ## Atribui a chave primária da Área de Atuação
        mainActingArea_ = ActingArea.objects.get(pk=request.data['mainActingArea'])
        institution_.mainActingArea = mainActingArea_

        ## Atribui a chave primária ao Responsável Técnico
        professional_ = Professional.objects.get(pk=request.data['technicalResponsible'])
        institution_.technicalResponsible = professional_

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
        webAddressList_ = request.data['webAddressList']
        for web_ in webAddressList_:
            web_inst = WebAddressInstitution(description=web_['description'],digital_address=web_['digital_address'],institution=institution_)
            web_inst.save()

        ##Retorna o objeto
        return Response({'id': institution_.pk})        
