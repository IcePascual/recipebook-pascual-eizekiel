from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeAddImageView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/<int:pk>/add_image', RecipeAddImageView.as_view(), name='recipe_add_image'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_create'),
]

app_name = 'ledger'
