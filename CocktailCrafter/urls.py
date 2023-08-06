"""
URL configuration for CocktailCrafter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cocktail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('alcohol', views.AlcoholList.as_view(), name="alcohollist"),
    path('alcohol/<pk>', views.AlcoholDetail.as_view(), name='alcoholdetail'),
    path('recipe', views.RecipeList.as_view(), name="recipelist"),
    path('recipe/<pk>', views.RecipeDetail.as_view(), name="recipedetail"),
    path('inventory', views.InventoryList.as_view(), name="inventorylist"),
    path('inventory/<pk>',
         views.InventoryDetail.as_view(),
         name="inventorydetail")
]
