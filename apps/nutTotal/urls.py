from django.urls import path

from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<slug>', RecipeDetailView.as_view(), name='recipe_detail'),
]