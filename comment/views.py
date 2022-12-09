# pylint: disable=no-member
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a comment if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    