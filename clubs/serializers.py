from rest_framework import serializers

from .models import Club

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    
    players = serializers.SlugRelatedField(
        slug_field='name',
        many=True, 
        read_only=True)

    coach = serializers.SlugRelatedField(
        slug_field = 'name',
        read_only = True,
        many = True
    )
    

    class Meta  :
        model = Club
        fields = ['id','name', 'country', 'state', 'coeff', 'formation', 'players', 'coach', 'created_at', 'updated_at']
