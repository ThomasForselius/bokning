from rest_framework import serializers
from rest_framework.response import Response
from .models import Booking

class BookingSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_image = serializers.ReadOnlyField(source='owner_profile.image')
    is_owner = serializers.SerializerMethodField()

    def get(self, request):
        serializer = BookingSerializer(Booking, many= True) 
        return Response(serializer.data)

    def get_is_owner(self, obj): 
        request = self.context['request']
        return request.user == obj.owner

    class Meta: 
        model = Booking 
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'date',
            'desc',
            'owner_image',
            'is_owner',
        ]