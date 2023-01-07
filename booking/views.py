# pylint: disable=no-member
from rest_framework import generics, permissions
from api.permissions import IsOwnerOrReadOnly
from .models import Booking
from .serializers import BookingSerializer

class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Booking.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a booking if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    