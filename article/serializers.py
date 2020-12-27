from rest_framework import serializers

from article.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        category = CategorySerializer()
        model = Product
        fields = '__all__'