from rest_framework.serializers import ModelSerializer

from recommender_section.models import RecommendedActivities, RecommendedActivitiesOffers


class RecommendedActivitiesSerializer (ModelSerializer):
    class Meta:
        model = RecommendedActivities
        fields = '__all__'


class RecommendedActivitiesOffersSerializer (ModelSerializer):
    class Meta:
        model = RecommendedActivitiesOffers
        fields = '__all__'

