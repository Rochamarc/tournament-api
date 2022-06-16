from rest_framework import serializers

from .models import SeasonIndividualPlayerStats

class SeasonIndividualPlayerStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonIndividualPlayerStats
        fields = ['id', 'season', 'competition', 'player_owner', 'club', 
        'goals', 'assists', 'shots_on_target', 'saves', 'hard_saves', 'tackles',
        'created_at','updated_at']