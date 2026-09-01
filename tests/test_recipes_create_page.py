from generators.recipe_data_for_tests import RecipeData
import allure

class TestRecipesCreatePage:
    @allure.title('Тест - проверяем, что карточка рецепта создается с правильным названием')
    def test_recipe_creation_successful(self, sign_in_page, top_menu, recipes_create_page, recipes_page, user):
        recipe = RecipeData().test_recipe
        sign_in_page.wait_for_sign_in_page_to_load()
        sign_in_page.sign_in_flow(email=user["username"], password=user["password"])
        recipes_page.wait_for_recipes_page_to_load()
        top_menu.click_on_create_recipe_button()
        recipes_create_page.wait_for_recipes_create_page_to_load()
        recipes_create_page.create_recipe_flow(recipe_name=recipe.name, ingredients=recipe.ingredients, cooking_time=recipe.cooking_time,
                                               recipe_description=recipe.description, image_path=recipe.image_path)
        recipes_create_page.wait_for_recipe_card_page_to_load()
        assert recipes_create_page.get_recipe_card_name() == recipe.name
