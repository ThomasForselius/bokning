# pylint: disable=no-member
from rest_framework import generics, filters
from api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
  
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'date',
        'owner',
        'receiver__username'
    ]
    ordering_fields = [
        'owner__username',
        'receiver__username',
        'date'
    ]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a comment if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    