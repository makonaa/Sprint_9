from pages.base_page import BasePage
from locators.recipes_create_page_locators import RecipesCreatePageLocators


class RecipesCreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipesCreatePageLocators()

    def wait_for_recipes_create_page_to_load(self):
        self.wait_for_element_to_appear(self.locators.RECIPE_CREATE_HEADER_LOCATOR)

    def fill_in_recipe_name_field(self, recipe_name:str):
        self.send_keys_to_input(self.locators.RECIPE_NAME_FIELD_LOCATOR, recipe_name)

    def fill_in_ingredient_field(self, ingredient:str):
        self.send_keys_to_input(self.locators.INGREDIENT_FIELD_LOCATOR, ingredient)

    def fill_in_ingredient_amount_field(self, ingredient_amount:int):
        self.send_keys_to_input(self.locators.INGREDIENT_AMOUNT_FIELD_LOCATOR, ingredient_amount)

    def click_on_add_ingredient_button(self):
        self.click_on_element(self.locators.ADD_INGREDIENT_BUTTON_LOCATOR)

    def wait_for_ingredient_list_to_load(self):
        self.wait_for_element_to_appear(self.locators.INGREDIENT_LIST_LOCATOR)

    def click_on_first_ingredient_button(self):
        self.click_on_element(self.locators.FIRST_INGREDIENT_IN_LIST_LOCATOR)

    def fill_in_ingredients(self, ingredients:dict):
        for ingredient_type, value in ingredients.items():
            self.fill_in_ingredient_field(ingredient_type)
            self.wait_for_ingredient_list_to_load()
            self.click_on_first_ingredient_button()
            self.fill_in_ingredient_amount_field(value)
            self.click_on_add_ingredient_button()

    def fill_in_cooking_time_field(self, cooking_time:int):
        self.send_keys_to_input(self.locators.COOKING_TIME_FIELD_LOCATOR, cooking_time)

    def fill_in_recipe_description_field(self, recipe_description:str):
        self.send_keys_to_input(self.locators.RECIPE_DESCRIPTION_FIELD_LOCATOR, recipe_description)

    def upload_recipe_photo(self, image_path:str):
        self.send_keys_to_input(self.locators.UPLOAD_FILE_INPUT_HIDDEN_LOCATOR, image_path)

    def click_on_create_recipe(self):
        self.click_on_element(self.locators.CREATE_RECIPE_BUTTON_LOCATOR)

    def wait_for_recipe_card_page_to_load(self):
        self.wait_for_element_to_appear(self.locators.RECIPE_CARD_NAME_LOCATOR)

    def get_recipe_card_name(self):
        return self.get_text_from_element(self.locators.RECIPE_CARD_NAME_LOCATOR)

    def create_recipe_flow(self, recipe_name, ingredients, cooking_time, recipe_description, image_path):
        self.fill_in_recipe_name_field(recipe_name)
        self.fill_in_ingredients(ingredients)
        self.fill_in_cooking_time_field(cooking_time)
        self.fill_in_recipe_description_field(recipe_description)
        self.upload_recipe_photo(image_path)
        self.click_on_create_recipe()
