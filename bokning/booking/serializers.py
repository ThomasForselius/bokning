from rest_framework import serializers
from rest_framework.response import Response
from .models import Booking

class BookingSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get(self, request):
        serializer = BookingSerializer(profiles, many= True) 
        return Response(serializer.data)

    def get_is_owner(self, obj): 
        request = self.context['request']
        return request.user == obj.owner

    class Meta: 
        model = Booking 
        fields = [
            'id',
            'owner',
            'is_owner',
            'created_at',
            'updated_at',
            'desc',
            'date',
        ]