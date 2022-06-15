from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player 
        fields = ['id', 'name', 'nationality', 'age', 'overall', 'current_club', 'position', 'matches', 'goals','assists', 
        'market_value', 'salary', 'height', 'weight', 'foot','average','created_at', 'updated_at' ]