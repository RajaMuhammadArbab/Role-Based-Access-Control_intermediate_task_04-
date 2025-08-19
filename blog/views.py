from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrEditorOwner



class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(is_deleted=False)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(is_deleted=False)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminOrEditorOwner]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()