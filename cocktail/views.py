import requests
from .cocktaildb import Cocktaildb

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Alcohol, Recipe, Ingredient, Inventory, Favorite


# Create your views here.
def home(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/random.php")
    if response.status_code == 200:
        data = response.json()
        context = {'cocktail': Cocktaildb(data['drinks'][0]).parse()}
        print(context)
    else:
        print(f"Request failed with status code: {response.status_code}")
    return render(request, 'cocktail/home.html', context)


class AlcoholList(ListView):
    model = Alcohol
    template_name = 'cocktail/alcohol_list.html'

    def get_context_data(self, **kwargs):
        # Call the superclass's get_context_data() to get the default context
        type = self.request.GET.get('type')
        context = super().get_context_data(**kwargs)
        types = Alcohol.objects.values_list('type', flat=True).distinct()
        # Add additional data to the context dictionary
        additional_data = {'types': types, 'type': type}
        context.update(additional_data)

        if type:
            context['alcohol_list'] = context['alcohol_list'].filter(type=type)
        return context


class AlcoholDetail(DetailView):
    model = Alcohol
    template_name = 'cocktail/alcohol_detail.html'
    context_object_name = 'alcohol'
