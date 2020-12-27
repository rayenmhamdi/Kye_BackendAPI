"""Kye_BackendAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Kye Inventory API DOC",
      default_version='v1',
      description="Kye Inventory Management System REST API simulator",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kye_support@kye.org"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('access/', include('access.urls')),
    path('crm/', include('crm.urls')),
    path('admin/', admin.site.urls),

    # Documentation paths
    url(r'^apidoc/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
