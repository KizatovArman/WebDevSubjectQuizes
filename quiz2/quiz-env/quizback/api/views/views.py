from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Contact
from api.serializers import ContactSerializer


class ContactListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Contact.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return ContactSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ContactsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(id=self.kwargs['pk'])

    def get_serializer_class(self):
        return ContactSerializer
