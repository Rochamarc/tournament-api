from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player 
        fields = ['name', 'nationality', 'age', 'overall', 'position', 'matches', 'goals','assists', 'created_at', 'updated_at' ]