from rest_framework import serializers

from .models import IndividualTrophy

class IndividualTrophySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndividualTrophy
        fields = ['id', 'season', 'competition', 'category', 'player_owner', 'created_at', 'updated_at']