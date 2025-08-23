from rest_framework import serializers

from .models import Recipe, Category, Heading

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'description',
            'thumbnail',
            'slug',
            'category',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'parent',
            'name',
            'title',
            'description',
            'thumbnail',
            'slug',
        ]

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = [
            'title',
            'slug',
            'level',
            'order',
        ]