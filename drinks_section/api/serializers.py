from rest_framework.serializers import ModelSerializer
from drinks_section.models import Drinks, IngestedDrinks

class DrinksSerializer(ModelSerializer):
    class Meta:
        model = Drinks
        fields = '__all__'


class IngestedDrinksSerializer(ModelSerializer):
    class Meta:
        model = IngestedDrinks
        fields = '__all__'
