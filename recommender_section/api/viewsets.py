from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from recommender_section.models import Offers
from recommender_section.api.serializers import OfferSerializer


class OfferViewSet(ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'begin_date', 'end_date', 'schedules', 'cost') #, 'locations__name', 'location__institution__name',
        # 'activities__description'
    # )



