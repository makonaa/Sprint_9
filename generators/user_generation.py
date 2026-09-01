from faker import Faker
import random
import string
import allure
from api_client import ApiClient


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def __get_random_str(self):
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(15))
        return random_str

    def __get_random_email(self) -> str:
        return f'{self.__get_random_str()}@{self.fake.free_email_domain()}'

    def __get_random_first_name(self) -> str:
        return self.fake.first_name()

    def __get_random_last_name(self) -> str:
        return self.fake.last_name()

    def __get_random_password(self) -> str:
        return self.fake.password()

    @allure.step('Создаем данные пользователя')
    def get_user_for_signup(self) -> dict:
        user_dict = {
            "email": self.__get_random_email(),
            "password": self.__get_random_password(),
            "first_name": self.__get_random_first_name(),
            "last_name": self.__get_random_last_name(),
            "username": self.__get_random_str()
        }
        return user_dict

class UserSignUp:
    def __init__ (self):
        self.user_data = DataGenerator().get_user_for_signup()
        self.api_client = ApiClient()

    @allure.step('Регистрируем пользователя')
    def signup_user(self):
        response = self.api_client.sign_up_user(self.user_data)
        if response.status_code != 201:
            raise Exception(f"Sign up for new user failed: {response.status_code}, {response.json()}")
        else:
            return self.user_data
