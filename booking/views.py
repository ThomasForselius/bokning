# pylint: disable=no-member
from rest_framework import generics, permissions, filters
from api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer

class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all().order_by('date')
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'date',
        'owner__username',
    ]
    ordering_fields = [
        'owner__username',
        'date'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a booking if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    