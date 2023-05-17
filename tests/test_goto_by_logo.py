from selenium import webdriver
from pages.main_page import MainPageScooter
from pages.order_page import OrderPage


class TestGotoByLogo:
    driver = None

    def test_goto_by_yandex_logo_from_main_page(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        main_page.wait_for_load_enter_button()
        assert main_page.current_url() == 'https://dzen.ru/?yredirect=true', "Новая страница не открылась"

    def test_goto_by_yandex_logo_from_order_page(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_header_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_load_header_for_whom_scooter()
        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        main_page.wait_for_load_enter_button()
        assert main_page.current_url() == 'https://dzen.ru/?yredirect=true', "Новая страница не открылась"

    def test_goto_scooter_logo_from_order_page(self, driver):
        main_page = MainPageScooter(driver)
        order_page = OrderPage(driver)
        main_page.click_header_order_button()
        order_page.wait_for_load_header_for_whom_scooter()
        main_page.click_scooter_logo()
        main_page.wait_for_scooter_img()
        assert 'Привезём его прямо к вашей двери' in main_page.header_main().text, "Переход на главную страницу не осуществлен"

