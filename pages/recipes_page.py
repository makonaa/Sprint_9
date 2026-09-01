from locators.recipes_page_locators import RecipesPageLocators
from pages.base_page import BasePage


class RecipesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipesPageLocators

    def wait_for_recipes_page_to_load(self):
        self.wait_for_element_to_appear(self.locators.RECIPES_HEADER_LOCATOR)
