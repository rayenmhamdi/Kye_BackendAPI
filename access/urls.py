from django.urls import path

from . import views
from .tokens import KyeObtainPairView

app_name = 'access'
urlpatterns = [
    path('token/', KyeObtainPairView.as_view(), name='token_obtain_pair'),
]