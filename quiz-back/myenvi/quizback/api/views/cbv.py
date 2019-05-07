from api.models import Post
from api.serializers import PostSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


class PostInfo(APIView):
    def get_object(self,pk):
        try:
            return True, Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return False, Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        have_found, result = self.get_object(pk)
        if have_found:
            serializer = PostSerializers(result)
            return Response(serializer.data)
        return result

    def put(self, request, pk):
        have_found, result = self.get_object(pk)
        if have_found:
            serializer = PostSerializers(instance=result, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return result

    def delete(self, request, pk):
        have_found, result = self.get_object(pk)
        if have_found:
            result.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return result

