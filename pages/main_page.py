from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators


class MainPageScooter(BasePage):

    def header_main(self):
        return self.driver.find_element(*MainPageLocators.main_header)
    def click_yandex_logo(self):
        element = self.driver.find_element(*BaseLocators.logo_yandex)
        self.click(element)

    def click_scooter_logo(self):
        element = self.driver.find_element(*BaseLocators.logo_scooter)
        self.click(element)

    def click_header_order_button(self):
        element = self.driver.find_element(*BaseLocators.order_button)
        self.click(element)

    def wait_for_load_enter_button(self):
        self.wait_element(BaseLocators.enter_button)

    def click_question_banner(self):
        element = self.driver.find_element(*MainPageLocators.question_field)
        self.click(element)

    def click_cookie_button(self):
        element = self.driver.find_element(*MainPageLocators.cookie_button)
        self.click(element)

    def scroll_to_order_button(self):
        element = self.driver.find_element(*MainPageLocators.order_button)
        self.scroll_to_element(element)

    def click_order_button(self):
        element = self.driver.find_element(*MainPageLocators.order_button)
        self.click(element)

    def scroll_to_header_main_questions(self):
        element = self.driver.find_element(*MainPageLocators.header_main_questions)
        self.scroll_to_element(element)

    def wait_for_load_header_main_questions(self):
        self.wait_element(MainPageLocators.header_main_questions)

    def wait_for_scooter_img(self):
        self.wait_element(MainPageLocators.scooter_img)

