from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from access.models import Licence

class EmailTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

class KyeObtainPairSerializer(EmailTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        token['role'] = user.profile.role
        token['theme'] = user.profile.theme
        token['licence'] = Licence.objects.get(pk=1).get_licences()

        return token


class KyeObtainPairView(TokenObtainPairView):
    serializer_class = KyeObtainPairSerializer

