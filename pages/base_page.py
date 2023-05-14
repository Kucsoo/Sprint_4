from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def logo_yandex(self):
        return self.driver.find_element(*BaseLocators.logo_yandex)

    def logo_scooter(self):
        return self.driver.find_element(*BaseLocators.logo_scooter)

    def header_order_button(self):
        return self.driver.find_element(*BaseLocators.order_button)



    def click_yandex_logo(self):
        self.logo_yandex().click()

    def click_scooter_logo(self):
        self.logo_scooter().click()

    def click_header_order_button(self):
        self.header_order_button().click()


    def current_url(self):
        return self.driver.current_url

    def wait_for_load_enter_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(BaseLocators.enter_button))

