from pages.base_page import BasePage
from locators.top_menu_locators import TopMenuLocators

class TopMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = TopMenuLocators()

    def wait_for_top_menu_to_load(self):
        self.wait_for_element_to_appear(self.locators.SIGN_UP_BUTTON_LOCATOR)

    def click_on_sign_up_button(self):
        self.click_on_element(self.locators.SIGN_UP_BUTTON_LOCATOR)

    def click_on_sign_in_button(self):
        self.click_on_element(self.locators.SIGN_IN_BUTTON_LOCATOR)

    def click_on_recipes_button(self):
        self.click_on_element(self.locators.RECIPES_BUTTON_LOCATOR)

    def is_exit_button_present(self):
        return self.is_element_visible(self.locators.EXIT_BUTTON_LOCATOR)

    def click_on_create_recipe_button(self):
        self.click_on_element(self.locators.CREATE_RECIPE_BUTTON_LOCATOR)
