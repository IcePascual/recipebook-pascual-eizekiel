from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe, Ingredient

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


def recipe(request, pk):
    recipe = Recipe.objects.get(pk)
    ctx = {'recipe': recipe}
    return render(request, 'ledger/recipe.html', ctx)


def ingredient(request, pk):
    ingredient = Ingredient.objects.get(pk)
    ctx = {'ingredient': ingredient}
    return render(request, 'ledger/ingredient.html', ctx)