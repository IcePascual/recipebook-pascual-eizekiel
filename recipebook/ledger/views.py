from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Recipe
from .forms import RecipeForm


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'recipe_list'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_create.html'
