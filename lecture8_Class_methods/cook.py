# example 4
class Recipe:
    all_recipes = []

    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
    
    def display_recipe(self):
        print(f"Recipe for {self.name}")
        print(f"Ingredients:")
        for ing in self.ingredients:
            print(f" - {ing}")
        print(f"Steps: {self.steps}")
        for step in self.steps:
            print(f" - {step}")

    @classmethod
    def display_all_recipes(cls):
        print(f"There are {len(cls.all_recipes)} recipes below:")
        for recipe in cls.all_recipes:
           print(recipe.name)

    @staticmethod
    def convert_to_g(amount, unit):
        if unit == "cups":
            return amount * 0.264172
        elif unit == "liters":
            return amount * 0.5
    

omelette = Recipe("Omelette", ["Eggs", "Cheese", "Milk", "Salt", "Pepper"], ["Crack eggs", "Mix ingredients", "Cook"])
cake = Recipe("Cake", ["Flour", "Sugar", "Eggs", "Butter", "Baking Powder"], ["Mix ingredients", "Bake"])
pasta = Recipe("Pasta", ["Pasta", "Tomato Sauce", "Cheese"], ["Boil pasta", "Add sauce", "Add cheese"])
fried_rice = Recipe("Fried Rice", ["Rice", "Eggs", "Soy Sauce", "Vegetables"], ["Cook rice", "Add ingredients", "Fry"])

omelette.display_recipe()
cake.display_recipe()
pasta.display_recipe()

Recipe.all_recipes.append(omelette)
Recipe.all_recipes.append(cake)
Recipe.all_recipes.append(pasta)
Recipe.all_recipes.append(fried_rice)

Recipe.display_all_recipes()

print(Recipe.convert_to_g(10, "cups"))