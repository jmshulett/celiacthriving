from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.views.generic import ListView

def recipe_list(request):
    recipes = Recipe.published.all()
    return render(request,
                 'recipes/list.html',
                 {'recipes': recipes})


def recipe_detail(request, year, month, day, post):
    recipes = get_object_or_404(Recipe, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'recipes/detail.html',
                  {'recipes': recipes})



class PostListView(ListView):
    queryset = Recipe.published.all()
    context_object_name = 'recipe'
    paginate_by = 3
    template_name = 'recipes/list.html'