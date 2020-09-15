from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from recommender_section.models import RecommendedActivities, RecommendedActivitiesOffers
from recommender_section.api.serializers import RecommendedActivitiesOffersSerializer, RecommendedActivitiesSerializer 

class RecommendedActivitiesViewSet(ModelViewSet):
    queryset = RecommendedActivities.objects.all()
    serializer_class = RecommendedActivitiesSerializer


class RecommendedActivitiesOffersViewSet(ModelViewSet):
    queryset = RecommendedActivitiesOffers.objects.all()
    serializer_class = RecommendedActivitiesOffersSerializer
