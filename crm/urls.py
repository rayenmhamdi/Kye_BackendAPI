from django.urls import path

from crm.views.client_views import ClientDetailsView, ClientCreateView
from crm.views.supplier_views import SupplierDetailsView, SupplierCreateView

app_name = 'crm'
urlpatterns = [
    path('clients/', ClientCreateView.as_view(), name="clients"),
    path('clients/<int:pk>/', ClientDetailsView.as_view(), name="client_details"),

    path('suppliers/', SupplierCreateView.as_view(), name="suppliers"),
    path('suppliers/<int:pk>/', SupplierDetailsView.as_view(), name="supplier_details"),
]