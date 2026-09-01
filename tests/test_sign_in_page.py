import Urls
import allure


class TestSignUpPage:
    @allure.title('Тест - проверяем, что логин успешно проходит для зарегистрированного юзера')
    def test_sign_in_with_existing_user_successful(self, top_menu, sign_in_page, recipes_page, user):
        top_menu.wait_for_top_menu_to_load()
        top_menu.click_on_sign_in_button()
        sign_in_page.wait_for_sign_in_page_to_load()
        #отправляем юзернейм, хотя на сайте написана почта, поскольку иначе логин не проходит
        sign_in_page.sign_in_flow(email=user["username"], password=user["password"])
        recipes_page.wait_for_recipes_page_to_load()
        assert (recipes_page.get_current_url() == Urls.RECIPES_URL) and (top_menu.is_exit_button_present())
