from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from crm.serializers import ClientSerializer
from crm.models import Client


class ClientCreateView(generics.ListCreateAPIView):
    """Get All and Create Clients"""
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new client."""
        serializer.save()


class ClientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests for a client."""
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


