from django.contrib import admin
from .models import Alcohol, Ingredient, Inventory, Favorite, Recipe

# Register your models here.
admin.site.register(Alcohol)
admin.site.register(Inventory)
admin.site.register(Ingredient)
admin.site.register(Favorite)
admin.site.register(Recipe)
