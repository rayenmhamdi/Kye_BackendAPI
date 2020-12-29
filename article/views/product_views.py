# Create your views here.


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from article.models import Product
from article.serializers import ProductSerializer



class ProductListCreateView(generics.ListCreateAPIView):
    """Create Product"""
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.order_by('-date_modified')
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new product."""
        serializer.save()

class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests for a product."""
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

