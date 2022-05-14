from rest_framework import viewsets

from .models import Trophy
from .serializers import TrophySerializer


class TrophyViewSet(viewsets.ModelViewSet):
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer
