from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from crm.serializers import SupplierSerializer
from crm.models import Supplier


class SupplierCreateView(generics.ListCreateAPIView):
    """Get All and Create suppliers"""
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new supplier."""
        serializer.save()


class SupplierDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests for a supplier."""
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


