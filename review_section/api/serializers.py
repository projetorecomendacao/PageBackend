from rest_framework.serializers import ModelSerializer
from review_section.models import Offer, Review


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
