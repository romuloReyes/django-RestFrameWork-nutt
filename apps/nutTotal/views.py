from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Recipe
from .serializers import RecipeListSerializer, RecipeSerializer

# Create your views here.
class RecipeListView(ListAPIView):
    queryset = Recipe.recipeObjects.all()
    serializer_class = RecipeListSerializer

class RecipeDetailView(RetrieveAPIView):
    queryset = Recipe.recipeObjects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'slug'