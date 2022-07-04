from rest_framework import serializers

from clubs.models import Club

from .models import Table

class ClubListing(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name']
        


class TableSerializer(serializers.HyperlinkedModelSerializer):
    
    club = ClubListing(many=False, read_only=False)

    class Meta:
        model = Table 
        fields = '__all__'

        '''
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
        '''
    
    def create(self, validated_data):
        data = validated_data.pop('club')
        club = Club.objects.filter(name=data['name'])[0]
        validated_data['club'] = club
        table = Table.objects.create(**validated_data)
        return table

