from rest_framework import serializers

from .models import Table

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table 
        fields = [
            'id',
            'season',
            'competition',
            'club',
            'points',
            'matches_played',
            'won',
            'draw',
            'lost',
            'goals_for',
            'goals_against',
            'goals_diff',
            'created_at', 
            'updated_at' 
            ]