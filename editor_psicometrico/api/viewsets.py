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


from esm_program_section.api.viewsets import Apoio
from editor_psicometrico.models import Documento, ActionsEditor
from editor_psicometrico.api.serializer import DocumentoSerializer
from utils.api.serializer import CustomModelViewSet, IsEditor

class DocumentoViewSet(CustomModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer 
    permission_classes_by_action = {
        'create': [IsEditor],
        'partial_update': [IsEditor],
        'destroy': [IsEditor],
        'update': [IsEditor]
    }

    @action(detail=True, methods=['post'],permission_classes=[IsEditor])
    def get_new(self, request, pk=None):
        id = request.data['id']
        actionId = request.data['action']
        lista = Documento.objects.filter(Q(id__gt= id),Q(active ='y')).order_by('id') 
        serializer = DocumentoSerializer(lista, many=True)   
        if (Documento.objects.count() == 0):
            biggerId = 0
        else:
            biggerId = Documento.objects.values('id').order_by('-id').first()['id']
        if (ActionsEditor.objects.count() == 0):
            biggerAction = 0
        else:    
            biggerAction = ActionsEditor.objects.values('id').order_by('-id').first()['id']
        volta = {'lista' : serializer.data, 'id' : biggerId, 'action' : biggerAction}
        return Response(volta)