from django.urls import path

from article.views.category_views import CategoryDetailsView, CategoryCreateView
from article.views.marque_views import MarqueDetailsView, MarqueCreateView
from article.views.product_views import ProductDetailsView, ProductListCreateView

app_name = 'article'
urlpatterns = [
    path('categories/', CategoryCreateView.as_view(), name="categories"),
    path('categories/<int:pk>/', CategoryDetailsView.as_view(), name="category_details"),

    path('marques/', MarqueCreateView.as_view(), name="marques"),
    path('marques/<int:pk>/', MarqueDetailsView.as_view(), name="marque_details"),

    path('products/', ProductListCreateView.as_view(), name="products"),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name="products_details"),

]