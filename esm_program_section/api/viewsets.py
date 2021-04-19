from django.db import models
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.utils.timezone import activate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from datetime import datetime
import json
from django.http import JsonResponse
from copy import copy

from utils.api.serializer import CustomModelViewSet, IsEditor
from esm_program_section.models import Event, Program, Intervention, ActiveEvent, ActionsEsm, EditorProgram
from esm_program_section.api.serializer import ProgramSerializer, InterventionSerializer, ActiveEventSerializer, ActionsEsmSerializer, EditorProgramSerializer

class EditorProgramViewSet(CustomModelViewSet):
    queryset = EditorProgram.objects.all()
    serializer_class = EditorProgramSerializer 
    permission_classes_by_action = {
        'create': [AllowAny],
        'partial_update': [IsEditor],
        'destroy': [IsEditor],
        'update': [IsEditor]
    }

    def create(self, request, *args, **kwargs):
        editor = EditorProgram.objects.filter(email=self.request.user.email)
        if editor.exists():
            editor = editor.first()
            serializer = self.get_serializer(editor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            editor = EditorProgram()
            editor.email = request.data['email']
            editor.name = request.data['name']
            editor.role = 'Teste'
            editor.save()
            serializer = self.get_serializer(editor)
            return Response(serializer.data, status=status.HTTP_200_OK)


class ActionsEsmViewSet(CustomModelViewSet):
    queryset = ActionsEsm.objects.all()
    serializer_class = ActionsEsmSerializer 
    permission_classes_by_action = {
        'create': [IsEditor],
        'partial_update': [IsEditor],
        'destroy': [IsEditor],
        'update': [IsEditor]
    }


class ProgramViewSet(CustomModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer 
    permission_classes_by_action = {
        'create': [IsEditor],   
        'partial_update': [IsEditor],
        'destroy': [IsEditor],
        'update': [IsEditor]
    }

    def partial_update(self, request, pk=None):
        ## vai ser utilizada para guardar o antigos valores do programa
        tProgram = copy(request.data)
        program = Program.objects.get(pk=pk)
        ## classe com o métodos de apoios
        apoio = Apoio()
        ##Este método atualiza os valores no programa e guarda os valores antigos do programa
        ##no tProgram, este valores serão guardados para quando for desfazer a ação
        apoio.atribui(program,request.data,tProgram)
        program.save()
        editor = EditorProgram.objects.get(email=request.user.email)        
        #Salva a ação realizada
        reg = {'old': tProgram, 'new' : request.data}
        action = apoio.grava('u','p',program.pk,0,0,editor,reg)
        return Response({'program' : pk, 'action' : action.pk})

    def create(self, request):
        program = Program()
        program.title = request.data['title']
        program.description = request.data['description']
        program.save()
        editor = EditorProgram.objects.get(email=request.user.email)
        apoio = Apoio()
        action = apoio.grava('c','p',program.pk,0,0,editor,request.data)
        return Response({'program' : program.pk, 'action' : action.pk})

    def list(self, request):
        queryset = Program.objects.filter(activate ='y').order_by('id')
        serializer = ProgramSerializer(queryset, many=True)
        if (Program.objects.count() == 0):
            biggerProgramId = 0
        else:
            biggerProgramId = Program.objects.values('id').order_by('-id').first()['id']
        if (ActionsEsm.objects.count() == 0):
            biggerActionId = 0
        else:    
            biggerActionId = ActionsEsm.objects.values('id').order_by('-id').first()['id']
        volta = {'lista' : serializer.data, 'program' : biggerProgramId, 'action' : biggerActionId, 'all'  : 'y'}
        return Response(volta)    

    @action(detail=True, methods=['post'],permission_classes=[IsEditor])
    def get_new(self, request, pk=None):
        print (request.data)
        idAction = request.data['idAction']
        idProgram = request.data['id']
        hasUpdate = ActionsEsm.objects.filter(Q(id__gt=idAction),Q(objectType = 'p'), Q(actionType = 'd') | Q(actionType = 'u'))
        all='n'
        lista=''
        if hasUpdate.exists():
            all='y'
            lista = Program.objects.filter(activate ='y').order_by('id')    
        else:
            lista = Program.objects.filter(Q(id__gt= idProgram),Q(activate ='y')).order_by('id') 
        serializer = ProgramSerializer(lista, many=True)   
        if (Program.objects.count() == 0):
            biggerProgramId = 0
        else:
            biggerProgramId = Program.objects.values('id').order_by('-id').first()['id']
        if (ActionsEsm.objects.count() == 0):
            biggerActionId = 0
        else:    
            biggerActionId = ActionsEsm.objects.values('id').order_by('-id').first()['id']
        volta = {'lista' : serializer.data, 'program' : biggerProgramId, 'action' : biggerActionId, 'all' : all }
        return Response(volta)

class ActiveEventViewSet(CustomModelViewSet):
    queryset = ActiveEvent.objects.all()
    serializer_class = ActiveEventSerializer 
    permission_classes_by_action = {
        'create': [IsEditor],
        'partial_update': [IsEditor],
        'destroy': [IsEditor],
        'update': [IsEditor]
    }

    ##o método atribui auxilia na atribuição dos valores do objeto 
    def atribui (self, model_, json_):
        for attr, value in json_.items():
            if (attr == 'program'):
                program = Program.objects.get(pk=value)
                model_.program = program
            else:
                setattr(model_, attr, value) 

    @action(detail=True, methods=['post'],permission_classes=[IsEditor])
    def get_new(self, request, pk=None):
        idEvent = request.data['idEvent']
        idProgram = Program.objects.get(pk=request.data['idProgram'])
        lista = ActiveEvent.objects.filter(Q(id__gt= idEvent),Q(activate ='y'),Q(program =idProgram)).order_by('id')
        serializer = ActiveEventSerializer(lista, many=True) 
        if (ActiveEvent.objects.count() == 0):  
            biggerEventId = 0
        else:
            biggerEventId = ActiveEvent.objects.values('id').order_by('-id').first()['id']
        if (ActionsEsm.objects.count() == 0):
            biggerActionId = 0
        else:
            biggerActionId = ActionsEsm.objects.values('id').order_by('-id').first()['id']
        program = ProgramSerializer(idProgram)
        volta = {'lista' : serializer.data, 'event' : biggerEventId, 'action' : biggerActionId, 'program' : program.data}
        return Response(volta)


    def list(self, request):
        queryset = ActiveEvent.objects.filter(activate ='y').order_by('id')
        serializer = ActiveEventSerializer(queryset, many=True)
        if (ActiveEvent.objects.count() == 0):  
            biggerEventId = 0
        else:
            biggerEventId = ActiveEvent.objects.values('id').order_by('-id').first()['id']
        if (ActionsEsm.objects.count() == 0):
            biggerActionId = 0
        else:
            biggerActionId = ActionsEsm.objects.values('id').order_by('-id').first()['id']
        volta = {'lista' : serializer.data, 'event' : biggerEventId, 'action' : biggerActionId, 'all'  : 'y'}
        return Response(volta)      

    def create(self, request):
        activEvent = ActiveEvent()
        #método que atribui os dados do evento
        self.atribui(activEvent,request.data)
        activEvent.save()
        program = request.data['program']
        editor = EditorProgram.objects.get(email=request.user.email)
        apoio = Apoio()
        action = apoio.grava('c','e',program,activEvent.pk,0,editor,request.data)
        return Response({'event' : activEvent.pk, 'action' : action.pk}) 

    def partial_update(self, request, pk=None):
        ## vai ser utilizada para guardar o antigos valores do programa
        tEvent = copy(request.data)
        print(tEvent)
        event = ActiveEvent.objects.get(pk=pk)
        ## classe com o métodos de apoios
        apoio = Apoio()
        ##Este método atualiza os valores no evento e guarda os valores antigos do evento
        ##no tEvent, este valores serão guardados para quando for desfazer a ação
        apoio.atribui(event,request.data,tEvent)
        print(tEvent)
        event.save()
        editor = EditorProgram.objects.get(email=request.user.email)        
        program = event.program.pk
        #Salva a ação realizada
        reg = {'old': tEvent, 'new' : request.data}
        action = apoio.grava('u','e',program,event.pk,0,editor,reg)
        serializer = ActiveEventSerializer(event)
        volta = serializer.data
        interventionsList = Intervention.objects.filter(event = event)
        interventios = InterventionSerializer(interventionsList,many=True).data

        return Response({'event' : volta, 'interventions' : interventios})   


class InterventionViewSet(CustomModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer 
    permission_classes_by_action = {
        'create': [IsEditor],
        'partial_update': [IsEditor],
        'destroy': [IsEditor],
        'update': [IsEditor]
    }

    ##o método atribui auxilia na atribuição dos valores do objeto 
    def atribui (self, model_, json_):
        for attr, value in json_.items():
            if (attr == 'event'):
                event = ActiveEvent.objects.get(pk=value)
                model_.event = event
            else:
                setattr(model_, attr, value) 

    ##Lista as intervenções que tẽm o id maior que a última intervenção enviada e que
    ##pertençam a um determinado ActiveEvent
    @action(detail=True, methods=['post'],permission_classes=[IsEditor])
    def get_new(self, request, pk=None):
        idIntervention = request.data['idIntervention']
        idEvent = ActiveEvent.objects.get(pk=request.data['idEvent'])
        lista = Intervention.objects.filter(Q(id__gt= idIntervention),Q(activate ='y'),Q(event =idEvent)).order_by('id')
        serializer = InterventionSerializer(lista, many=True) 
        if (Intervention.objects.count() == 0):  
            biggerInterventionId = 0
        else:
            biggerInterventionId = Intervention.objects.values('id').order_by('-id').first()['id']
        if (ActionsEsm.objects.count() == 0):
            biggerActionId = 0
        else:
            biggerActionId = ActionsEsm.objects.values('id').order_by('-id').first()['id']
        event = ActiveEventSerializer(idEvent).data
        volta = {'lista' : serializer.data, 'intervention' : biggerInterventionId, 'action' : biggerActionId, 'event' : event}
        return Response(volta)

    def list(self, request):
        queryset = Intervention.objects.filter(activate ='y').order_by('id')
        serializer = InterventionSerializer(queryset, many=True)
        if (Intervention.objects.count() == 0):  
            biggerInterventionId = 0
        else:
            biggerInterventionId = Intervention.objects.values('id').order_by('-id').first()['id']
        if (ActionsEsm.objects.count() == 0):
            biggerActionId = 0
        else:
            biggerActionId = ActionsEsm.objects.values('id').order_by('-id').first()['id']
        volta = {'lista' : serializer.data, 'intervention' : biggerInterventionId, 'action' : biggerActionId, 'all'  : 'y'}
        return Response(volta)      

    def create(self, request):
        #cria a lista de intervenções que foram criadas antes da que está sendo criada..
        idIntervention = request.data['idIntervention']
        idEvent = ActiveEvent.objects.get(pk=request.data['idEvent'])
        lista = Intervention.objects.filter(Q(id__gt= idIntervention),Q(activate ='y'),Q(event =idEvent)).order_by('id')
        listaSerializer = InterventionSerializer(lista, many=True) 
        #salva a intervenção
        intervention = Intervention()
        #método que atribui os dados do evento
        self.atribui(intervention,request.data['intervention'])
        intervention.event = idEvent
        intervention.save()
        #Salva a operação no action
        event = request.data['idEvent']
        program = ActiveEvent.objects.get(pk=event).program.pk
        editor = EditorProgram.objects.get(email=request.user.email)
        apoio = Apoio()
        action = apoio.grava('c','i',program,event,intervention.pk,editor,request.data)
        eventSerializer = ActiveEventSerializer(event)
        return Response({'intervention' : intervention.pk, 'action' : action.pk, 'lista' : listaSerializer.data, 'event' : eventSerializer.data}) 

    def partial_update(self, request, pk=None):
        ## vai ser utilizada para guardar o antigos valores do programa
        tIntervention = copy(request.data)
        intervention = Intervention.objects.get(pk=pk)
        ## classe com o métodos de apoios
        apoio = Apoio()
        ##Este método atualiza os valores no evento e guarda os valores antigos do evento
        ##no tIntervention, este valores serão guardados para quando for desfazer a ação
        apoio.atribui(intervention,request.data,tIntervention)
        intervention.save()
        editor = EditorProgram.objects.get(email=request.user.email)    
        event = intervention.event.pk    
        program = ActiveEvent.objects.get(pk=event).program.pk
        #Salva a ação realizada
        reg = {'old': tIntervention, 'new' : request.data}
        action = apoio.grava('u','i',program,event,intervention.pk,editor,reg)
        serializer = InterventionSerializer(intervention)
        return Response(serializer.data)  

class Apoio:
    def grava (self,actionType, objectType, programPk, eventPk, interventionPk, editor, anterior):
        locAction = ActionsEsm()
        locAction.actionType = actionType
        locAction.editor = editor
        locAction.objectType = objectType
        locAction.program_id = programPk
        locAction.event_id = eventPk
        locAction.intervention_id = interventionPk
        locAction.anterior = anterior
        locAction.save()
        return locAction

    ##o método atribui auxilia na criação com um objeto com o valor anterior das 
    ##alterações parciais
    def atribui (self, model_, json_,copia_):
        for attr, value in json_.items():
            setattr(model_, attr, value) 
 
   