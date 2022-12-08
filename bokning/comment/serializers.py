from rest_framework import serializers
from rest_framework.response import Response
from .models import Comment

class CommentSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    booking = serializers.ReadOnlyField(source='booking.date')
    is_owner = serializers.SerializerMethodField()

    def get(self, request):
        serializer = CommentSerializer(Comment, many= True) 
        return Response(serializer.data)

    def get_is_owner(self, obj): 
        request = self.context['request']
        return request.user == obj.owner

    class Meta: 
        model = Comment 
        fields = [
            'id',
            'owner',
            'is_owner',
            'created_at',
            'updated_at',
            'desc',
        ]