from rest_framework.response import Response
from rest_framework import status

from participant_section.models import Participant, ParticipantSituation
from experts_section.models import Expert
from page_usp_section.models_1_psicologico_usp import NegativeAttitudesAgingUsp, CognitionDeficitUsp, DepressionUsp, PsychologicalAspectsUsp
from page_usp_section.models_2_Biologicos_usp import BiologicalAspectsUsp, SensoryDeficitUsp, FunctionalDisabilityUsp, MalnutritionUsp, CardiovascularFactorsUsp, MisuseMedicationsUsp
from page_usp_section.models_3_sociais_usp import SocialAspectsUsp, LowSocialSupportUsp, EnvironmentalProblemsUsp, ViolenceUsp
from page_usp_section.models_4_multidimensional_usp import MultidisciplinaryDomainUsp, FallsUsp
from page_usp_section.models_0_page_usp import PageUsp
from page_usp_section.api.serializers import NegativeAttitudesAgingUspSerializer, CognitionDeficitUspSerializer,\
    DepressionUspSerializer, PsychologicalAspectsUspSerializer, BiologicalAspectsUspSerializer, SensoryDeficitUspSerializer,\
    FunctionalDisabilityUspSerializer, MalnutritionUspSerializer, CardiovascularFactorsUspSerializer,\
    MisuseMedicationsUspSerializer, SocialAspectsUspSerializer, LowSocialSupportUspSerializer, EnvironmentalProblemsUspSerializer,\
    ViolenceUspSerializer, MultidisciplinaryDomainUspSerializer, FallsUspSerializer, PageUspSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert
from assessment_section.models import DemandMap
from datetime import datetime
import json
from django.http import JsonResponse


class NegativeAttitudesAgingViewSetUsp(CustomModelViewSet):
    queryset = NegativeAttitudesAgingUsp.objects.all()
    serializer_class = NegativeAttitudesAgingUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CognitionDeficitViewSetUsp(CustomModelViewSet):
    queryset = CognitionDeficitUsp.objects.all()
    serializer_class = CognitionDeficitUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class DepressionViewSetUsp(CustomModelViewSet):
    queryset = DepressionUsp.objects.all()
    serializer_class = DepressionUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PsychologicalAspectsViewSetUsp(CustomModelViewSet):
    queryset = PsychologicalAspectsUsp.objects.all()
    serializer_class = PsychologicalAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class BiologicalAspectsViewSetUsp(CustomModelViewSet):
    queryset = BiologicalAspectsUsp.objects.all()
    serializer_class = BiologicalAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SensoryDeficitViewSetUsp(CustomModelViewSet):
    queryset = SensoryDeficitUsp.objects.all()
    serializer_class = SensoryDeficitUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FunctionalDisabilityViewSetUsp(CustomModelViewSet):
    queryset = FunctionalDisabilityUsp.objects.all()
    serializer_class = FunctionalDisabilityUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MalnutritionViewSetUsp(CustomModelViewSet):
    queryset = MalnutritionUsp.objects.all()
    serializer_class = MalnutritionUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CardiovascularFactorsViewSetUsp(CustomModelViewSet):
    queryset = CardiovascularFactorsUsp.objects.all()
    serializer_class = CardiovascularFactorsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MisuseMedicationsViewSetUsp(CustomModelViewSet):
    queryset = MisuseMedicationsUsp.objects.all()
    serializer_class = MisuseMedicationsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SocialAspectsViewSetUsp(CustomModelViewSet):
    queryset = SocialAspectsUsp.objects.all()
    serializer_class = SocialAspectsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class LowSocialSupportViewSetUsp(CustomModelViewSet):
    queryset = LowSocialSupportUsp.objects.all()
    serializer_class = LowSocialSupportUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class EnvironmentalProblemsViewSetUsp(CustomModelViewSet):
    queryset = EnvironmentalProblemsUsp.objects.all()
    serializer_class = EnvironmentalProblemsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class ViolenceViewSetUsp(CustomModelViewSet):
    queryset = ViolenceUsp.objects.all()
    serializer_class = ViolenceUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MultidisciplinaryDomainViewSetUsp(CustomModelViewSet):
    queryset = MultidisciplinaryDomainUsp.objects.all()
    serializer_class = MultidisciplinaryDomainUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FallsViewSetUsp(CustomModelViewSet):
    queryset = FallsUsp.objects.all()
    serializer_class = FallsUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PageViewSetUsp(CustomModelViewSet):
    queryset = PageUsp.objects.all()
    serializer_class = PageUspSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert]
    }


    def get_queryset(self):
        # Define um filtro para retornar apenas os pages do gerontologista logado
        gerontologist = Expert.objects.get(email=self.request.user.email)
        return PageUsp.objects.filter(gerontologist=gerontologist)


    ## Monta e retorna do objeto PAGe
    def retrieve(self, request, pk=None):
        page_ = PageUsp.objects.get(id = pk)

        if page_.psychologicalAspects:
            psi = PsychologicalAspectsUsp.objects.filter(pk = page_.psychologicalAspects.pk).values()
            psi_ = list(psi)
           
            dados= CognitionDeficitUsp.objects.filter(pk = page_.psychologicalAspects.cognition_deficit.pk).values()
            cognitionDeficit = list(dados)

            dados = NegativeAttitudesAgingUsp.objects.filter(pk = page_.psychologicalAspects.negative_attitudes_aging.pk).values()
            negativeAttitudesAging  = list(dados)

            dados = DepressionUsp.objects.filter(pk = page_.psychologicalAspects.depression.pk).values()
            depression = list(dados)

        else:
            psi_ = [{'id' : -1}]
            cognitionDeficit = [{'id' : -1}]
            negativeAttitudesAging = [{'id' : -1}]
            depression = [{'id' : -1}]
        

        if page_.biologicalAspects:
            # Biologicos
            bio = BiologicalAspectsUsp.objects.filter(pk = page_.biologicalAspects.pk).values()
            bio_ = list(bio)

            dados = SensoryDeficitUsp.objects.filter(pk = page_.biologicalAspects.sensoryDeficit.pk).values()
            sensoryDeficit = list(dados)

            dados  = FunctionalDisabilityUsp.objects.filter(pk = page_.biologicalAspects.functionalDisability.pk).values()
            functionalDisability = list(dados)

            dados = MalnutritionUsp.objects.filter(pk = page_.biologicalAspects.malNutrition.pk).values()
            malnutrition = list(dados)

            dados = CardiovascularFactorsUsp.objects.filter(pk = page_.biologicalAspects.cardiovascularFactors.pk).values()
            cardiovascularFactors = list(dados)

            dados =  MisuseMedicationsUsp.objects.filter(pk = page_.biologicalAspects.misuseMedications.pk).values()
            misuseMedications = list(dados)

        else:
            bio_ = [{'id' : -1}]
            sensoryDeficit = [{'id' : -1}]
            functionalDisability = [{'id' : -1}]
            malnutrition = [{'id' : -1}]
            cardiovascularFactors = [{'id' : -1}]
            misuseMedications = [{'id' : -1}]
        
        if page_.socialAspects:

            # Social Aspects
            soc = SocialAspectsUsp.objects.filter(pk = page_.socialAspects.pk).values()
            soc_ = list(soc)

            dados = LowSocialSupportUsp.objects.filter(pk = page_.socialAspects.lowSocialSupport.pk).values()
            lowSocialSupport = list(dados)

            dados = EnvironmentalProblemsUsp.objects.filter(pk = page_.socialAspects.environmentalProblems.pk).values()
            environmentalProblems = list(dados)

            dados = ViolenceUsp.objects.filter(pk = page_.socialAspects.violence.pk).values()
            violence = list(dados)

        else :
            soc_ = [{'id' : -1}]
            lowSocialSupport = [{'id' : -1}]
            environmentalProblems = [{'id' : -1}]
            violence = [{'id' : -1}]


        if page_.multidisciplinaryDomain:
            
            mul = MultidisciplinaryDomainUsp.objects.filter(pk = page_.multidisciplinaryDomain.pk).values()
            mul_ = list(mul)

            dados  = FallsUsp.objects.filter(pk = page_.multidisciplinaryDomain.falls.pk).values()
            falls = list(dados)

        else:
            mul_ = [{'id' : -1}]
            falls = [{'id' : -1}]

        if page_.participant_situation:
            #Situação participant
            dados = ParticipantSituation.objects.filter(pk = page_.participant_situation.pk).values()
            participanteSituation = list(dados)
        else:
            participanteSituation = [{'id' : -1}]

        if page_.demandMap:
            #demand map
            dados = DemandMap.objects.filter(pk = page_.demandMap.pk).values()
            demandMap = list(dados)
        else : 
            demandMap = [{'id' : -1}]

        #cabeça page
        cabecaPage = {
            'id' : page_.pk,
            'service' : page_.service,
            'entrance' : page_.entrance,
            'interviewed' : page_.interviewed,
            'interviewer' : page_.interviewer,
            'avaliation_date' : page_.avaliation_date,
            'created_at' : page_.created_at,
            'updated_at' : page_.updated_at,
            'start_time' : page_.start_time,
            'end_time' : page_.end_time,
            'gerontologist' : page_.gerontologist.pk,
        }

        return Response ({'cognitionDeficit' : cognitionDeficit,
            'negativeAttitudesAging' : negativeAttitudesAging,
            'depression' : depression,
            'sensoryDeficit' : sensoryDeficit,
            'functionalDisability' : functionalDisability,
            'malnutrition' : malnutrition,
            'cardiovascularFactors' : cardiovascularFactors,
            'misuseMedications' : misuseMedications,
            'lowSocialSupport' : lowSocialSupport,
            'environmentalProblems' : environmentalProblems,
            'violence' : violence,
            'falls' : falls,
            'participanteSituation' : participanteSituation,
            'demandMap' : demandMap,
            'cabecaPage' : cabecaPage,
            'psi' : psi_,
            'bio' : bio_,
            'soc' : soc_,
            'mul' : mul_
         })

    ##o método atribui auxilia no preenchimento dos valores dos objetos no create e no update
    def atribui (self, model_, json_):
        for attr, value in json_.items():
            setattr(model_, attr, value)    

    # O método de gravação foi criado de modo a gravar o Page por partes ou inteiro, 
    # Antes de gravar qualquer uma das seções ele verifica se a seção está presente no objeto page 
    # que veio do frontend..
    def create(self,request, *args, **kwargs):
        # Dados do cabecalho do page
        cabecaPage_ = request.data['cabecaPage']
        participant_situation_ = request.data['participant_situation']
        psychologicalAspects_ = request.data['psychologicalAspects']
        biologicalAspects_ = request.data['biologicalAspects']
        socialAspects_ = request.data['socialAspects']
        multidisciplinaryDomain_ = request.data['multidisciplinaryDomain']
        demandMap_ = request.data['demandMap']

        #Localiza o participant
        participant_ = Participant.objects.get(id = request.data["participant_id"])

        #Localiza o especialista
        gerontologist_ = Expert.objects.get(id = request.data["gerontologist_id"])
        
        #inicia o objeto page
        page = PageUsp()

        # Atribui os valores do cabeçalho do PAGe
        self.atribui(page,cabecaPage_)
        # Acerta os valores dos campos data do cabeçalho
        page.avaliation_date = datetime.strptime(cabecaPage_['avaliation_date'],'%Y-%m-%d')
        page.entrance = datetime.strptime(cabecaPage_['entrance'],'%Y-%m-%d')
        
        #Atribui o participante
        page.participant = participant_
        
        #Atribui o especialista
        page.gerontologist = gerontologist_
        
        #gravar situação do participant
        if 'estaVazio' not in participant_situation_.keys():
            base =  ParticipantSituation()
            self.atribui(base,participant_situation_)
            base.save()
            page.participant_situation = base

        #gravar os aspectos psicológicos
        if 'estaVazio' not in psychologicalAspects_.keys():
            psi = PsychologicalAspectsUsp()
            #Déficit cognitivo
            base =  CognitionDeficitUsp()
            self.atribui(base,psychologicalAspects_['cognitiveDeficitForm'])
            base.save()
            psi.cognition_deficit = base
            
            #depressão
            base =  DepressionUsp()
            self.atribui(base,psychologicalAspects_['depressionForm'])
            base.save()
            psi.depression = base

            #Atitutes negativas em relação ao envelhecimento
            base =  NegativeAttitudesAgingUsp()
            self.atribui(base,psychologicalAspects_['negativeAttitudesAgingForm'])
            base.save()
            psi.negative_attitudes_aging = base

            #salva os aspectos psicológicos
            psi.comments = psychologicalAspects_['commentsForm']['comments']
            psi.save()

            page.psychologicalAspects = psi

        #gravar os aspectos biológicos
        if 'estaVazio' not in biologicalAspects_.keys():   
            bio = BiologicalAspectsUsp()
            #Fatores Cardiovasculares     
            base =  CardiovascularFactorsUsp()
            self.atribui(base,biologicalAspects_['cardiovascularFactorsForm'])
            base.save()
            bio.cardiovascularFactors = base

            #Incapacidades Funcionais     
            base =  FunctionalDisabilityUsp()
            self.atribui(base,biologicalAspects_['functionalDisabilityForm'])
            base.save()
            bio.functionalDisability = base

            #Desnutrição     
            base =  MalnutritionUsp()
            self.atribui(base,biologicalAspects_['malnutritionForm'])
            base.save()
            bio.malNutrition = base

            #Uso incorreto de medicamentos
            base =  MisuseMedicationsUsp()
            self.atribui(base,biologicalAspects_['misuseMedicationsForm'])
            base.save()
            bio.misuseMedications = base
            
            #Déficit Sensorial
            base =  SensoryDeficitUsp()
            self.atribui(base,biologicalAspects_['sensoryDeficitForm'])
            base.save()
            bio.sensoryDeficit = base

            #salvar os aspectos biológicos
            bio.comments = biologicalAspects_['commentsForm']['comments']
            bio.save()

            page.biologicalAspects = bio
        
        #gravar os aspectos sociais
        if 'estaVazio' not in socialAspects_.keys():   
            soc = SocialAspectsUsp()
            #Baixo suporte social
            base =  LowSocialSupportUsp()
            self.atribui(base,socialAspects_['lowSocialSupportForm'])
            base.save()
            soc.lowSocialSupport = base

            #Problemas ambientais
            base =  EnvironmentalProblemsUsp()
            self.atribui(base,socialAspects_['environmentalProblemsForm'])
            base.save()
            soc.environmentalProblems = base

            #Violência
            base =  ViolenceUsp()
            self.atribui(base,socialAspects_['violenceForm'])
            base.save()
            soc.violence = base

            soc.comments = socialAspects_['commentsForm']['comments']
            soc.save()

            page.socialAspects = soc

        #gravar os aspectos multidimensionais
        if 'estaVazio' not in multidisciplinaryDomain_.keys():   
            mul = MultidisciplinaryDomainUsp()
            #Quedas
            base =  FallsUsp()
            self.atribui(base,multidisciplinaryDomain_['fallsForm'])
            base.save()
            mul.falls = base

            mul.comments = multidisciplinaryDomain_['commentsForm']['comments']
            mul.save()

            page.multidisciplinaryDomain = mul

        #grava mapa de demanda
        if 'estaVazio' not in demandMap_.keys():   
            dema = DemandMap()
            self.atribui(dema, demandMap_)
            dema.save()

            page.demandMap = dema                        

        page.save()

        return Response ({'id': page.pk})


    def update(self, request, pk=None):
        # Dados do Page colocado em cada dimensão
        cabecaPage_ = request.data['cabecaPage']
        participant_situation_ = request.data['participant_situation']
        psychologicalAspects_ = request.data['psychologicalAspects']
        biologicalAspects_ = request.data['biologicalAspects']
        socialAspects_ = request.data['socialAspects']
        multidisciplinaryDomain_ = request.data['multidisciplinaryDomain']
        demandMap_ = request.data['demandMap']

        # Busca o PAGe no banco de dados
        page_ = PageUsp.objects.get(id = pk)

        #prepara os dados de retorno
        volta = {'page' : pk, 'psi' : -1, 'bio' : -1, 'soc' : -1, 'mul' : -1, 'par' : -1 , 'map' : -1}

        #Verifica se veio os dados da situação do participante
        if 'estaVazio' not in participant_situation_.keys():
            if page_.participant_situation:
                #atualiza a situação do participante com os dados que vieram do frontend
                self.atribui(page_.participant_situation,participant_situation_)
                page_.participant_situation.save()
            else:
                #Caso o PAGe não tenha a situação do participante cria-se uma
                base = ParticipantSituation()
                #atribui ao novo membro os dados que vieram do frontend
                self.atribui(base,participant_situation_)
                #salva
                base.save()
                #atribui ao PAGe
                page_.participant_situation = base
                #Atualiza a volta
                volta['par'] = base.pk   

        #gravar os aspectos psicológicos
        if 'estaVazio' not in psychologicalAspects_.keys():
            if page_.psychologicalAspects:
                #Caso o PAGe possua os aspectos psicológicos ele será atualizado
                psi = PsychologicalAspectsUsp.objects.get(pk = page_.psychologicalAspects.pk)
                #Atualiza o déficit cognitivo
                base= CognitionDeficitUsp.objects.get(id = psi.cognition_deficit.pk)
                dados= psychologicalAspects_['cognitiveDeficitForm']
                self.atribui(base,dados)
                base.save()

                #Atualiza Atitudes Negativas em relação ao processo de envelhecimento
                dados= psychologicalAspects_['negativeAttitudesAgingForm']	
                base =  NegativeAttitudesAgingUsp.objects.get(id = psi.negative_attitudes_aging.pk)
                self.atribui(base,dados)
                base.save()        

                #Atualiza os dados da depressão
                dados= psychologicalAspects_['depressionForm']	
                base =  DepressionUsp.objects.get(id = psi.depression.pk)
                self.atribui(base,dados)
                base.save()        
                
                dados= psychologicalAspects_["commentsForm"]	
                psi.comments_psico = dados["comments"]
                psi.save()
                volta['psi'] = psi.pk
            else:
                #Caso o page ainda não tenha os aspectos psicológicos, será criado um..
                psi = PsychologicalAspectsUsp()
                #Déficit cognitivo
                base =  CognitionDeficitUsp()
                self.atribui(base,psychologicalAspects_['cognitiveDeficitForm'])
                base.save()
                psi.cognition_deficit = base
                
                #depressão
                base =  DepressionUsp()
                self.atribui(base,psychologicalAspects_['depressionForm'])
                base.save()
                psi.depression = base

                #Atitutes negativas em relação ao envelhecimento
                base =  NegativeAttitudesAgingUsp()
                self.atribui(base,psychologicalAspects_['negativeAttitudesAgingForm'])
                base.save()
                psi.negative_attitudes_aging = base

                #salva os aspectos psicológicos
                psi.comments = psychologicalAspects_['commentsForm']['comments']
                psi.save()

                page_.psychologicalAspects = psi

        # Gravar os aspectos biológicos se vieram
        if 'estaVazio' not in biologicalAspects_.keys():  
            if page_.biologicalAspects :
                #Caso o PAGe possua os aspectos biológico
                bio = BiologicalAspectsUsp.objects.get(pk = page_.biologicalAspects.pk)
                
                # Atualiza o déficit sensorial
                dados = biologicalAspects_["sensoryDeficitForm"]	
                base =  SensoryDeficitUsp.objects.get(pk = bio.sensoryDeficit.pk)
                self.atribui(base,dados)
                base.save()        
            
                #Atualiza as incapacidades funcionais
                dados = biologicalAspects_["functionalDisabilityForm"]	
                base =  FunctionalDisabilityUsp.objects.get(pk = bio.functionalDisability.pk)
                self.atribui(base,dados)
                base.save()        
                
                #Atualiza a desnutrição
                dados = biologicalAspects_["malnutritionForm"]	
                base =  MalnutritionUsp.objects.get(pk = bio.malNutrition.pk)
                self.atribui(base,dados)
                base.save()        
                
                #Atualiza os fatores Cardiovasculares
                dados = biologicalAspects_["cardiovascularFactorsForm"]	
                base =  CardiovascularFactorsUsp.objects.get (pk = bio.cardiovascularFactors.pk)
                self.atribui(base,dados)
                base.save()        
                
                #Atualiza o Mau uso de medicamentos
                dados = biologicalAspects_["misuseMedicationsForm"]	
                base =  MisuseMedicationsUsp.objects.get (pk = bio.misuseMedications.pk)
                self.atribui(base,dados)
                base.save()        
                
                dados = biologicalAspects_["commentsForm"]	
                bio.comments_bio = dados["comments"]
                bio.save()
                volta['bio'] = bio.pk
            
            else:

                bio = BiologicalAspectsUsp()
                #Fatores Cardiovasculares     
                base =  CardiovascularFactorsUsp()
                self.atribui(base,biologicalAspects_['cardiovascularFactorsForm'])
                base.save()
                bio.cardiovascularFactors = base

                #Incapacidades Funcionais     
                base =  FunctionalDisabilityUsp()
                self.atribui(base,biologicalAspects_['functionalDisabilityForm'])
                base.save()
                bio.functionalDisability = base

                #Desnutrição     
                base =  MalnutritionUsp()
                self.atribui(base,biologicalAspects_['malnutritionForm'])
                base.save()
                bio.malNutrition = base

                #Uso incorreto de medicamentos
                base =  MisuseMedicationsUsp()
                self.atribui(base,biologicalAspects_['misuseMedicationsForm'])
                base.save()
                bio.misuseMedications = base
                
                #Déficit Sensorial
                base =  SensoryDeficitUsp()
                self.atribui(base,biologicalAspects_['sensoryDeficitForm'])
                base.save()
                bio.sensoryDeficit = base

                #salvar os aspectos biológicos
                bio.comments = biologicalAspects_['commentsForm']['comments']
                bio.save()
                volta['bio'] = bio.pk
                page_.biologicalAspects = bio

        # Gravar os aspectos sociais caso existam
        if 'estaVazio' not in socialAspects_.keys():   
            # Caso o page já tenha os aspectos sociais
            if page_.socialAspects:
                #Pega o aspecto social do PAGe    
                soc = SocialAspectsUsp.objects.get(pk = page_.socialAspects.pk)

                #Atualiza o baixo suporte social
                dados = socialAspects_["lowSocialSupportForm"]	
                base =  LowSocialSupportUsp.objects.get (pk = soc.lowSocialSupport.pk)
                self.atribui(base,dados)
                base.save()        
                
                #Atualiza os problemas ambientais
                dados = socialAspects_["environmentalProblemsForm"]	
                base =  EnvironmentalProblemsUsp.objects.get(pk = soc.environmentalProblems.pk)
                self.atribui(base,dados)
                base.save()        
                
                #Atualiza Violência
                dados = socialAspects_["violenceForm"]	
                base =  soc.violence;
                self.atribui(base,dados)
                base.save()        
                
                
                dados = socialAspects_["commentsForm"]	
                soc.comments_social = dados["comments"]
                soc.save()
                volta['soc'] = soc.pk

            else: 
                #Cria um novo aspectos sociais
                soc = SocialAspectsUsp()
                #Baixo suporte social
                base =  LowSocialSupportUsp()
                self.atribui(base,socialAspects_['lowSocialSupportForm'])
                base.save()
                soc.lowSocialSupport = base

                #Problemas ambientais
                base =  EnvironmentalProblemsUsp()
                self.atribui(base,socialAspects_['environmentalProblemsForm'])
                base.save()
                soc.environmentalProblems = base

                #Violência
                base =  ViolenceUsp()
                self.atribui(base,socialAspects_['violenceForm'])
                base.save()
                soc.violence = base

                soc.comments = socialAspects_['commentsForm']['comments']
                soc.save()
                volta['soc'] = soc.pk
                page_.socialAspects = soc

        if 'estaVazio' not in multidisciplinaryDomain_.keys(): 
            if page_.multidisciplinaryDomain:
                
                mul = page_.multidisciplinaryDomain
                dados = multidisciplinaryDomain_["fallsForm"]	
                base =  mul.falls
                self.atribui(base,dados)
                base.save()        

                dados = multidisciplinaryDomain_["commentsForm"]	
                mul.comments_multi = dados["comments"]        
                mul.save()
                volta['mul'] = mul.pk

            else:
                mul = MultidisciplinaryDomainUsp()
                #Quedas
                base =  FallsUsp()
                self.atribui(base,multidisciplinaryDomain_['fallsForm'])
                base.save()
                mul.falls = base

                mul.comments = multidisciplinaryDomain_['commentsForm']['comments']
                mul.save()

                page_.multidisciplinaryDomain = mul                
                volta['mul'] = mul.pk

        #grava mapa de demanda
        if 'estaVazio' not in demandMap_.keys():   
            if page_.demandMap:
                dados = demandMap_
                base = page_.demandMap
                self.atribui(base,dados)
                base.save()      
                volta['map'] = base.pk
            else:            
                dema = DemandMap()
                self.atribui(dema, demandMap_)
                dema.save()
                page_.demandMap = dema 
                volta['map'] = dema.pk       


        page_.service = cabecaPage_['service']
        page_.entrance= datetime.strptime(cabecaPage_['entrance'],'%Y-%m-%d')
        page_.interviewed= cabecaPage_['interviewed']
        page_.interviewer= cabecaPage_['interviewer']
        page_.avaliation_date= datetime.strptime(cabecaPage_['avaliation_date'],'%Y-%m-%d')
        page_.end_time = cabecaPage_['end_time']
        page_.start_time = cabecaPage_['start_time'] 	
        
        page_.save()


        return Response (volta)