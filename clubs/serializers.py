from rest_framework import serializers

from .models import Club

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta  :
        model = Club
        fields = ['name', 'country', 'state', 'coeff', 'formation', 'created_at', 'updated_at']