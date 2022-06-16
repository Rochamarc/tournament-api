from rest_framework import viewsets

from .models import IndividualTrophy
from .serializers import IndividualTrophySerializer


class IndividualTrophyViewSet(viewsets.ModelViewSet):
    queryset = IndividualTrophy.objects.all()
    serializer_class = IndividualTrophySerializer
