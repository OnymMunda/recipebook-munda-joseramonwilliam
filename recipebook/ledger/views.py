from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ledger.models import Recipe

class RecipeListView(ListView):
	model = Recipe  
	template_name = "recipes_list.html"

class RecipeDetailView(DetailView):
	model = Recipe
	template_name = "recipe.html"