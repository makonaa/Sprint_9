from selenium.webdriver.common.by import By

class SignInPageLocators:
    SIGN_IN_HEADER_LOCATOR = (By.XPATH, '//h1[text()="Войти на сайт"]')
    SIGN_IN_FORM_BUTTON_LOCATOR = (By.XPATH, '//form/button[text()="Войти"]')
    EMAIL_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
