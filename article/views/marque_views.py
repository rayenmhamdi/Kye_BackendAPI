# Create your views here.


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from article.models import  Marque
from article.serializers import MarqueSerializer


class MarqueCreateView(generics.ListCreateAPIView):
    """Get All and Create Categories"""
    permission_classes = [IsAuthenticated]
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new category."""
        serializer.save()


class MarqueDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests for a marque."""
    permission_classes = [IsAuthenticated]
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer