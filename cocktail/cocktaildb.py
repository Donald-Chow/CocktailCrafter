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
