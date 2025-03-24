from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


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


class RecipeAddImageView(CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'ledger/recipe_add_image.html'
    
    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={ 'pk': self.kwargs['pk'] })
