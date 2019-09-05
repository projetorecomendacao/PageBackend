from django.http import QueryDict
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from experts_section.models import Expert, Expertise
from experts_section.api.serializers import ExpertiseSerializer, ExpertSerializer
from utils.api.serializer import CustomModelViewSet


class ExpertViewSet(CustomModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)
    permission_classes_by_action = {
        'create': [AllowAny]
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


class ExpertiseViewSet(ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)

