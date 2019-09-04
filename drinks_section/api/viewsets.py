from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drinks_section.models import Drinks, IngestedDrinks
from drinks_section.api.serializers import DrinksSerializer, IngestedDrinksSerializer

class DrinksViewSet(ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer



class IngestedDrinksViewSet(ModelViewSet):
    queryset = IngestedDrinks.objects.all()
    serializer_class = IngestedDrinksSerializer

