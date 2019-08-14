from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from review_section.models import Offer, Review
from review_section.api.serializers import OfferSerializer, ReviewSerializer


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'begin_date', 'end_date', 'schedules', 'cost') #, 'locations__name', 'location__institution__name',
        # 'activities__description'
    # )


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('rate', 'date') #, 'activity__description')
