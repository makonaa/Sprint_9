from selenium.webdriver.common.by import By


class SignUpPageLocators:
    SIGN_UP_HEADER_LOCATOR = (By.XPATH, '//h1[text()="Регистрация"]')
    FIRST_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="first_name"]')
    LAST_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="last_name"]')
    USERNAME_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="username"]')
    EMAIL_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
    CREATE_ACCOUNT_FORM_BUTTON_LOCATOR = (By.XPATH, '//form/button[text()="Создать аккаунт"]')
