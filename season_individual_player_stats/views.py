from rest_framework import viewsets

from .models import SeasonIndividualPlayerStats
from .serializers import SeasonIndividualPlayerStatsSerializer


class SeasonIndividualPlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = SeasonIndividualPlayerStats.objects.all()
    serializer_class = SeasonIndividualPlayerStatsSerializer
