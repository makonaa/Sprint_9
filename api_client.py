import requests
import Urls
import allure


class ApiClient:
    @allure.step('Отправляем API запрос регистрации юзера')
    def sign_up_user(self, user_data: dict) -> requests.Response:
        return requests.post(Urls.SIGN_UP_API_URL, data=user_data)
