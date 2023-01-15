# pylint: disable=no-member
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

@login_required
class ProfileList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
@login_required
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    