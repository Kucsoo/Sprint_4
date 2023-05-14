from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
class MainPageScooter:
    def __init__(self, driver):
        self.driver = driver
    def question_banner(self):
        return self.driver.find_element(*MainPageLocators.question)

    def header_main(self):
        return self.driver.find_element(*MainPageLocators.main_header)
    def header_main_questions(self):
        return self.driver.find_element(*MainPageLocators.header_main_questions)

    def click_question_banner(self):
        self.question_banner().click()

    def cookie_button(self):
        return self.driver.find_element(*MainPageLocators.cookie_button)

    def click_cookie_button(self):
        self.cookie_button().click()

    def order_button(self):
        return self.driver.find_element(*MainPageLocators.order_button)

    def scroll_to_order_button(self):
        element = self.order_button()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_button(self):
        self.order_button().click()


    def scroll_to_header_main_questions(self):
        element = self.header_main_questions()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_load_header_main_questions(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_field))
    def wait_for_scooter_img(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.scooter_img))

