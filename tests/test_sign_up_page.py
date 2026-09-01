from generators.user_generation import DataGenerator
import Urls
import allure


class TestSignUpPage:
    @allure.title('Тест - проверяем, что регистрация юзера проходит успешно')
    def test_sign_up_successful(self, top_menu, sign_up_page, sign_in_page):
        user_data = DataGenerator().get_user_for_signup()
        top_menu.wait_for_top_menu_to_load()
        top_menu.click_on_sign_up_button()
        sign_up_page.wait_for_sign_up_page_to_load()
        sign_up_page.fill_in_sign_up_form_and_create_acc(first_name = user_data['first_name'], last_name = user_data['last_name'],
                                                         username = user_data['username'], email = user_data['email'], password = user_data['password'])
        sign_in_page.wait_for_sign_in_page_to_load()
        assert (sign_in_page.get_current_url() == Urls.SIGN_IN_URL) and sign_in_page.is_sign_in_form_visible()
