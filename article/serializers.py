from rest_framework import serializers

from article.models import Category, Product, Marque


class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product_number = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('product_number',)


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('category_name',)

"""
class GetLanguageSerializer(serializers.ModelSerializer):
    technology = serializers.StringRelatedField(many=True)
    frameworks = serializers.StringRelatedField(many=True)

    total_technology = serializers.SerializerMethodField(read_only=True)
    toatl_frameworks = serializers.SerializerMethodField(read_only=True)

    def get_toatl_frameworks(self, language):
        return language.frameworks.count()

    def get_total_technology(self, language):
        return language.technology.count() # change 'technology' with corresponding "related_name" value

    class Meta:
        model = Language
        fields = (other_fileds, 'total_technology', 'toatl_frameworks')
        depth = 1
"""