from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from experts_section.models import Expert,Expertise
from experts_section.api.serializers import ExpertiseSerializer,ExpertSerializer

class ExpertViewSet(ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description')


class ExpertiseViewSet(ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)

