# pylint: disable=no-member
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer

class CommentList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a comment if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    