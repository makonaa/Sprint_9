import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import Urls
from pages.recipes_create_page import RecipesCreatePage
from pages.recipes_page import RecipesPage
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage
from pages.top_menu import TopMenu
from generators.user_generation import UserSignUp


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options
    )
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def top_menu(driver):
    return TopMenu(driver)

@pytest.fixture
def sign_up_page(driver):
    return SignUpPage(driver)

@pytest.fixture
def sign_in_page(driver):
    return SignInPage(driver)

@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)

@pytest.fixture
def recipes_create_page(driver):
    return RecipesCreatePage(driver)

@pytest.fixture
def user():
    user_data = UserSignUp().signup_user()
    return user_data
