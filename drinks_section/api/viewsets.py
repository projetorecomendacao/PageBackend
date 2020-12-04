from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drinks_section.models import Drinks, IngestedDrinks
from drinks_section.api.serializers import DrinksSerializer, IngestedDrinksSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert

class DrinksViewSet(CustomModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer



class IngestedDrinksViewSet(CustomModelViewSet):
    queryset = IngestedDrinks.objects.all()
    serializer_class = IngestedDrinksSerializer

