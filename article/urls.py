from django.urls import path

from article.views.category_views import CategoryDetailsView, CategoryCreateView
from article.views.product_views import ProductCreateView

app_name = 'article'
urlpatterns = [
    path('categories/', CategoryCreateView.as_view(), name="categories"),
    path('categories/<int:pk>/', CategoryDetailsView.as_view(), name="category_details"),

    path('products/', ProductCreateView.as_view(), name="products"),
]