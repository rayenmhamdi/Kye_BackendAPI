# Create your views here.


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from article.models import Category, Product
from article.serializers import CategorySerializer, ProductSerializer


class ProductCreateView(generics.ListCreateAPIView):
    """Get All and Create Products"""
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new product."""
        serializer.save()

