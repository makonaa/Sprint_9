from selenium.webdriver.common.by import By


class RecipesCreatePageLocators:
    RECIPE_CREATE_HEADER_LOCATOR = (By.XPATH, '//h1[text()="Создание рецепта"]')
    RECIPE_NAME_FIELD_LOCATOR = (By.XPATH, '//div[text()="Название рецепта"]/../input')
    ADD_INGREDIENT_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'div[class*="styles_ingredientAdd"]')
    INGREDIENT_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[class*="styles_ingredientsInput"]')
    INGREDIENT_LIST_LOCATOR = (By.CSS_SELECTOR, 'div[class*="styles_ingredientsInputs"] div[class*="styles_container"]')
    FIRST_INGREDIENT_IN_LIST_LOCATOR = (By.CSS_SELECTOR, 'div[class*="styles_ingredientsInputs"] div[class*="styles_container"] div:first-of-type')
    INGREDIENT_AMOUNT_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[class*="styles_ingredientsAmountValue"]')
    COOKING_TIME_FIELD_LOCATOR = (By.XPATH, '//div[text()="Время приготовления"]/../input')
    RECIPE_DESCRIPTION_FIELD_LOCATOR = (By.CSS_SELECTOR, 'textarea[class*="styles_textareaField"]')
    UPLOAD_FILE_INPUT_HIDDEN_LOCATOR = (By.CSS_SELECTOR, 'input[class*="styles_fileInput"]')
    CREATE_RECIPE_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Создать рецепт"]')
    EDIT_RECIPE_BUTTON_LOCATOR = (By.XPATH, '//a[text()="Редактировать рецепт"]')
    RECIPE_CARD_NAME_LOCATOR = (By.CSS_SELECTOR, 'h1[class*="styles_single-card__title"]')
