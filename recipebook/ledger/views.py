from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe, Ingredient


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'


def recipe(request, pk):
    recipe = Recipe.objects.get(pk)
    ctx = {'recipe': recipe}
    return render(request, 'ledger/recipe.html', ctx)
