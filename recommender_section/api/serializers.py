from rest_framework.serializers import ModelSerializer
from recommender_section.models import Offers


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'


