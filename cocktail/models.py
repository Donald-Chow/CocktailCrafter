from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Alcohol(models.Model):
    cdbid = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(default="")
    type = models.CharField(max_length=100, default="Others")
    alcoholic = models.BooleanField(null=True)
    abv = models.IntegerField(null=True)


class Recipe(models.Model):
    cdbid = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=100)
    instructions = models.TextField(default="")
    alcoholic = models.BooleanField(null=True)
    glass = models.CharField(max_length=100)
    drinkThumb = models.URLField(default="")


class Ingredient(models.Model):
    alcohol = models.ForeignKey(Alcohol, on_delete=models.RESTRICT)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    measure = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(null=True)
    unit = models.CharField(max_length=100, default="")


class Inventory(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             blank=False,
                             null=False)
    alcohol = models.ForeignKey(Alcohol,
                                on_delete=models.RESTRICT,
                                blank=False,
                                null=False)
    quantity = models.IntegerField(blank=False, null=False)
    unit = models.CharField(max_length=100)


class Favorite(models.Model):
    user = models.ForeignKey(User,
                             blank=False,
                             null=False,
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,
                               blank=False,
                               null=False,
                               on_delete=models.RESTRICT)
    note = models.TextField(default="")
