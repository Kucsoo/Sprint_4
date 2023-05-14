from selenium import webdriver
from pages.base_page import BasePage
from pages.main_page import MainPageScooter
from pages.order_page import OrderPage

class TestGotoByLogo:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_goto_by_yandex_logo_from_main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.click_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[1])
        base_page.wait_for_load_enter_button()
        assert base_page.current_url() == 'https://dzen.ru/?yredirect=true', "Новая страница не открылась"

    def test_goto_by_yandex_logo_from_order_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.click_header_order_button()
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_header_for_whom_scooter()
        base_page.click_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[2])
        base_page.wait_for_load_enter_button()
        assert base_page.current_url() == 'https://dzen.ru/?yredirect=true', "Новая страница не открылась"

    def test_goto_scooter_logo_from_order_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        main_page = MainPageScooter(self.driver)
        order_page = OrderPage(self.driver)
        base_page.click_header_order_button()
        order_page.wait_for_load_header_for_whom_scooter()
        base_page.click_scooter_logo()
        main_page.wait_for_scooter_img()
        assert 'Привезём его прямо к вашей двери' in main_page.header_main().text, "Переход на главную страницу не осущестлен"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()