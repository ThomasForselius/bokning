# pylint: disable=no-member
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from .models import Booking
from .serializers import BookingSerializer

class BookingList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    