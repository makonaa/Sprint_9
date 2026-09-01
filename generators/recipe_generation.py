class Recipe:
    def __init__(self, name:str, ingredients:dict, cooking_time:int, description:str, image_path:str):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.description = description
        self.image_path = image_path


class RecipeBuilder:
    def __init__(self):
        self.name = 'TestName'
        self.ingredients = {}
        self.cooking_time = 0
        self.description = ''
        self.image_path = ''

    def with_recipe_name(self, name:str):
        self.name = name
        return self

    def with_ingredient_and_amount(self, ingredient:str, amount:int):
        self.ingredients[ingredient] = amount
        return self

    def with_cooking_time(self, cooking_time:int):
        self.cooking_time = cooking_time
        return self

    def with_description(self, description:str):
        self.description = description
        return self

    def with_image_path(self, image_path:str):
        self.image_path = image_path
        return self

    def build(self):
        return Recipe(name=self.name, ingredients=self.ingredients, cooking_time=self.cooking_time, description=self.description, image_path=self.image_path)
