# pylint: disable=no-member
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly, IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    