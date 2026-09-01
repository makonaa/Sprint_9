from locators.sign_up_page_locators import SignUpPageLocators
from pages.base_page import BasePage

class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignUpPageLocators()

    def wait_for_sign_up_page_to_load(self):
        self.wait_for_element_to_appear(self.locators.SIGN_UP_HEADER_LOCATOR)

    def fill_first_name_field(self, first_name:str):
        self.send_keys_to_input(self.locators.FIRST_NAME_INPUT_LOCATOR, first_name)

    def fill_last_name_field(self, last_name:str):
        self.send_keys_to_input(self.locators.LAST_NAME_INPUT_LOCATOR, last_name)

    def fill_username_field(self, username:str):
        self.send_keys_to_input(self.locators.USERNAME_INPUT_LOCATOR, username)

    def fill_email_field(self, email:str):
        self.send_keys_to_input(self.locators.EMAIL_INPUT_LOCATOR, email)

    def fill_password_field(self, password:str):
        self.send_keys_to_input(self.locators.PASSWORD_INPUT_LOCATOR, password)

    def click_on_create_account_button(self):
        self.click_on_element(self.locators.CREATE_ACCOUNT_FORM_BUTTON_LOCATOR)

    def fill_in_sign_up_form_and_create_acc(self, first_name:str, last_name:str, username:str, email:str, password:str):
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_username_field(username)
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_on_create_account_button()
