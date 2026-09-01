from pages.base_page import BasePage
from locators.sign_in_page_locators import SignInPageLocators


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignInPageLocators()

    def wait_for_sign_in_page_to_load(self):
        self.wait_for_element_to_appear(SignInPageLocators.SIGN_IN_HEADER_LOCATOR)

    def is_sign_in_form_visible(self):
        return self.is_element_visible(self.locators.SIGN_IN_FORM_BUTTON_LOCATOR)

    def fill_email_field(self, email:str):
        self.send_keys_to_input(self.locators.EMAIL_INPUT_LOCATOR, keys=email)

    def fill_password_field(self, password:str):
        self.send_keys_to_input(self.locators.PASSWORD_INPUT_LOCATOR, keys=password)

    def click_sign_in_button(self):
        self.click_on_element(self.locators.SIGN_IN_FORM_BUTTON_LOCATOR)

    def sign_in_flow(self, email:str, password:str):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_sign_in_button()
