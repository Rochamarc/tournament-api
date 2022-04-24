from rest_framework import serializers

from .models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game 
        fields = [
            'competition',
            'season',
            'hour',
            'home_team',
            'away_team',
            'score',
            'stadium',
            'home_shots',
            'home_shots_on_target',
            'home_fouls',
            'home_tackles',
            'home_saves',
            'home_ball_possession',
            'home_offsides',
            'home_freekicks',
            'away_shots',
            'away_shots_on_target',
            'away_fouls',
            'away_tackles',
            'away_saves',
            'away_ball_possession',
            'away_offsides',
            'away_freekicks',
            'created_at',
            'updated_at'
        ]