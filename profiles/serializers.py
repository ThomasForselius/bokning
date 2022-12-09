from rest_framework import serializers
from rest_framework.response import Response
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get(self, request):
        serializer = ProfileSerializer(profiles, many= True) 
        return Response(serializer.data)

    def get_is_owner(self, obj): 
        request = self.context['request']
        return request.user == obj.owner

    class Meta: 
        model = Profile 
        fields = [
            'id',
            'owner',
            'is_owner',
            'created_at',
            'updated_at',
            'name',
            'image',
        ]