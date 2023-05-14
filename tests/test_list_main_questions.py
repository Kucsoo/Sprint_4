import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageScooter

class TestAnswersAndQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
    @pytest.mark.parametrize('question, answer, result',
                             [[0, 0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                              [1, 1, 'Пока что у нас так: один заказ — один самокат. '
                                  'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                              [2, 2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите '
                                     'заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                              [3, 3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                              [4, 4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                              [5, 5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                              [6, 6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                              [7, 7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']])
    def test_check_answers(self, question, answer, result):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageScooter(self.driver)
        main_page.scroll_to_header_main_questions()
        method, locator = MainPageLocators.question_field
        locator = locator.format(question)
        question_field = self.driver.find_element(method, locator)
        method, locator = MainPageLocators.answer_field
        locator = locator.format(answer)
        answer_field = self.driver.find_element(method, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", answer_field)
        question_field.click()
        WebDriverWait(self.driver, 9).until(
            expected_conditions.visibility_of(answer_field))
        answer_field = self.driver.find_element(method, locator)
        assert answer_field.text == result, "Ответ не появился"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



