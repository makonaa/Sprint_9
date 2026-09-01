from generators.recipe_generation import RecipeBuilder
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "pancakes.jpg")

class RecipeData:
    test_recipe = RecipeBuilder().with_recipe_name('Панкейки').with_ingredient_and_amount(ingredient='молоко', amount=250).with_ingredient_and_amount(ingredient='мука', amount=300).with_cooking_time(30).with_description('вкусные панкейки').with_image_path(image_path).build()
