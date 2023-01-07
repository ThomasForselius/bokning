from rest_framework import serializers
from rest_framework.response import Response
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    booking = serializers.ReadOnlyField(source='booking.date')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get(self, request):
        serializer = CommentSerializer(Comment, many= True) 
        return Response(serializer.data)

    def get_is_owner(self, obj): 
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
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