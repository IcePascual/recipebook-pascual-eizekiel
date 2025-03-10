from django.contrib import admin

from .models import Recipe, RecipeIngredient


# Register your models here.
class IngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [IngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
