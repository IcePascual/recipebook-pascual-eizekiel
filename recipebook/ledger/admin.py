from django.contrib import admin

from .models import Recipe, RecipeIngredient, RecipeImage


# Register your models here.
class IngredientInline(admin.TabularInline):
    model = RecipeIngredient


class ImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        IngredientInline,
        ImageInline]


admin.site.register(Recipe, RecipeAdmin)
