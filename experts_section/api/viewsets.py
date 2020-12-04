from django.db import models
from django.http import QueryDict
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from experts_section.models import Expert, Expertise, Orientador
from experts_section.api.serializers import ExpertiseSerializer, ExpertSerializer, OrientadorSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert
from django.db.models import Count
from page_usp_section.models_0_page_usp import PageUsp


class ExpertViewSet(CustomModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [AllowAny],
        'getSelf': [IsExpert]
    }

    def create(self, request, *args, **kwargs):
        expert = Expert.objects.filter(email=self.request.user.email)
        if expert.exists():
            expert = expert.first()
            serializer = self.get_serializer(expert)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = {
                'email': request.user.email,
                'name': request.user.first_name + ' ' + request.user.last_name
            }
            request._full_data = data
            return super().create(request, args, kwargs)

    @action(detail=False, methods=['post'])
    def getSelf(self, request, *args, **kwargs):
        me = Expert.objects.get(email=request.user.email)
        serializer = self.get_serializer(me)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExpertiseViewSet(CustomModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)



class OrientadorViewSet(CustomModelViewSet):
    queryset = Orientador.objects.all()
    serializer_class = OrientadorSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert],
        'update': [IsExpert],
    }

    #método que verifica se existe o e-mail do aluno
    def achaEmailAluno(self, email):
        ori_teste = Orientador.objects.filter(
            models.Q(orientando_email = email) | \
            models.Q(dupla_email = email) ) 
        if ori_teste.exists(): #Verifica se o email já está cadastrado no orientandos
            return True
        return False

    def get_queryset(self):
        # Define um filtro para retornar a quantidade de pages de cada orientando.
        oris = Orientador.objects.all()
        for ori in oris:
            oriUp = Orientador.objects.get(pk=ori.pk)
            oriUp.qtdPages = PageUsp.objects.filter(gerontologist=ori.orientando_id).count()
            oriUp.save()
        volta = Orientador.objects.all()
        return volta

    def create(self, request, *args, **kwargs):
        #Verifica se o email do aluno já está cadastrado
        if self.achaEmailAluno(request.data['orientando_email']): #Verifica se o email já está cadastrado no orientandos
            return Response({'id' : -1})
        else:
            #Verifica se o email da dupla já está cadastrado
            if self.achaEmailAluno(request.data['dupla_email']):
                return Response({'id' : -2})
            else:
                ori = Orientador()
                ori.orientador = Expert.objects.get(pk=1) # Por Enquanto Vai ser todo mundo da Ruth
                ori.orientando_email = request.data['orientando_email']
                ori.orientando_name = request.data['orientando_name']
                ori.dupla_name = request.data['dupla_name']
                ori.dupla_email = request.data['dupla_email']
                ori.trio_name = request.data['trio_name']
                expert = Expert.objects.filter(email=request.data['orientando_email'])
                if expert.exists():
                    #Não deixa salvar se o e-mail já existe nos experts
                    return Response({'id' : -1})
                    #expert = expert.first()
                    #expert.name = request.data['orientando_name']
                    #expert.save()
                    #ori.orientando_id = expert
                else:
                    exp = Expert()
                    exp.name = request.data['orientando_name']
                    exp.email = request.data['orientando_email']
                    exp.save()
                    ori.orientando_id = exp
                ori.save()
                return Response({'id' : ori.pk})
    

    def update(self, request, pk=None):
        ori = Orientador.objects.get(id = pk)
        #Verifica se mudou o email e o novo já está cadastrado no orientandos
        if (ori.orientando_email != request.data['orientando_email']):
            if self.achaEmailAluno(request.data['orientando_email']): 
                return Response({'id' : -1})
            #Verifica se tem alguem que já usa o e-mail
            expert = Expert.objects.filter(email=request.data['orientando_email'])
            if expert.exists():
                return Response({'id' : -1})

        #Verifica se mudou o email e o novo já está cadastrado no orientandos
        if (ori.dupla_email != request.data['dupla_email']):
            if self.achaEmailAluno(request.data['dupla_email']):
                return Response({'id' : -2})               

        exp = Expert.objects.get (id = ori.orientando_id.pk)
        exp.name = request.data['orientando_name']
        exp.email = request.data['orientando_email']
        exp.save()
        ori.orientando_email = request.data['orientando_email']
        ori.orientando_name = request.data['orientando_name']
        ori.dupla_name = request.data['dupla_name']
        ori.dupla_email = request.data['dupla_email']
        ori.trio_name = request.data['trio_name']
        ori.save()
        return Response({'id' : ori.pk})        

