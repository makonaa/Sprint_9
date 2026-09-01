from selenium.webdriver.common.by import By

class TopMenuLocators:
    SIGN_UP_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'a[href="/signup"]')
    SIGN_IN_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'header[class*="style_header"] a[href="/signin"]')
    RECIPES_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'header[class*="style_header"] a[href="/recipes"]')
    EXIT_BUTTON_LOCATOR = (By.XPATH, '//a[text()="Выход"]')
    CREATE_RECIPE_BUTTON_LOCATOR = (By.XPATH, '//a[text()="Создать рецепт"]')
