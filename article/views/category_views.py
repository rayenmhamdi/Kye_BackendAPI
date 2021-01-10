from django.shortcuts import render

# Create your views here.


from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Category
from article.serializers import CategorySerializer


class CategoryCreateView(generics.ListCreateAPIView):
    """Get All and Create Categories"""
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new category."""
        serializer.save()


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests for a category."""
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.products.count() > 0:
            return Response(data={'message': "CAT_01"},
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)




