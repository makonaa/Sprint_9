from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def wait_for_element_to_appear(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def get_text_from_element(self, locator):
        element_text = self.driver.find_element(*locator).text
        return element_text

    def get_current_url(self):
        return self.driver.current_url
