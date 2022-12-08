from rest_framework import serializers
from rest_framework.response import Response
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    
    def get(self, request):
        serializer = ProfileSerializer(profiles, many= True) 
        return Response(serializer.data)

    class Meta: 
        model = Profile 
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'image',
        ]