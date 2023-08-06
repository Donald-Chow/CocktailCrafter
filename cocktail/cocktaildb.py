class Cocktaildb:

    def __init__(self, data):
        self.cocktail = data

    def parse(self):
        ingredients = []
        for n in range(1, 16):
            if self.cocktail['strIngredient' + str(n)]:
                ingredients.append({
                    'name':
                    self.cocktail['strIngredient' + str(n)],
                    'measure':
                    self.cocktail['strMeasure' + str(n)]
                })

        return {
            'cdbid': self.cocktail['idDrink'],
            'name': self.cocktail['strDrink'],
            'category': self.cocktail['strCategory'],
            'instructions': self.cocktail['strInstructions'],
            'alcoholic': self.cocktail['strAlcoholic'],
            'glass': self.cocktail['strGlass'],
            'drinkThumb': self.cocktail['strDrinkThumb'],
            'ingredients': ingredients
        }


# Storing Alcohol Seed here
# def seed():
#     n = 1
#     while n <= 616:
#         response = requests.get(
#             "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid=" +
#             str(n))
#         if response.json()['ingredients']:
#             data = response.json()['ingredients'][0]
#             cdbid = data['idIngredient']
#             name = data['strIngredient']
#             print("creating" + name)
#             if data['strDescription']:
#                 description = data['strDescription']
#             else:
#                 description = ""
#             if data['strType']:
#                 type = data['strType']
#             else:
#                 type = "Others"
#             alcoholic = (data['strAlcohol'] == "Yes")
#             if data['strABV']:
#                 abv = int(data['strABV'])
#             else:
#                 abv = 0
#             Alcohol(cdbid=cdbid,
#                     name=name,
#                     description=description,
#                     type=type,
#                     alcoholic=alcoholic,
#                     abv=abv).save()
#         n += 1
