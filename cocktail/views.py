from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Alcohol, Recipe, Ingredient, Inventory, Favorite


# Create your views here.
def home(request):
    return render(request, 'cocktail/home.html')


class AlcoholList(ListView):
    model = Alcohol
    template_name = 'cocktail/alcohol_list.html'


class AlcoholDetail(DetailView):
    model = Alcohol
    template_name = 'cocktail/alcohol_detail.html'
    context_object_name = 'alcohol'
