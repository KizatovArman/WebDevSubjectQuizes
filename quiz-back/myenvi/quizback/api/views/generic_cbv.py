from api.models import Post
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from api.serializers import PostSerializers, UserSerializer
from rest_framework import mixins

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Post.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
