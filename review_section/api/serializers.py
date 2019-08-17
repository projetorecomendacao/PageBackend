from rest_framework.serializers import ModelSerializer
from review_section.models import Offers, Review


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
