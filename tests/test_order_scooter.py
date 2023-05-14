from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.main_page import MainPageScooter

class TestMakeOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_make_order_header_button_without_comment_success(self, name, surname, address, telephone):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        order_page = OrderPage(self.driver)
        base_page.click_header_order_button()
        order_page.wait_for_load_header_for_whom_scooter()
        order_page.click_name()
        order_page.set_name(name)
        order_page.click_surname()
        order_page.set_surname(surname)
        order_page.click_address()
        order_page.set_address(address)
        order_page.click_metro_station_choose()
        order_page.click_metro_station()
        order_page.click_phone()
        order_page.set_phone(telephone)
        order_page.click_button_next()
        order_page.wait_for_load_header_about_rent()
        order_page.click_date()
        order_page.click_day()
        order_page.click_rent_duration()
        order_page.click_option_of_list_rent_duration()
        order_page.click_scooter_color()
        order_page.click_checkbox_black()
        order_page.click_order_button()
        order_page.wait_for_load_order_modal_window()
        order_page.click_yes_button()
        order_page.wait_for_load_header_modal_window()
        assert "Номер заказа" in order_page.header_pop_up().text, "Заказ не оформлен"

    def test_make_order_main_page_button_with_comment_success(self, name, surname, address, telephone, comment):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        main_page = MainPageScooter(self.driver)
        main_page.scroll_to_order_button()
        main_page.click_order_button()
        order_page.wait_for_load_header_for_whom_scooter()
        order_page.click_name()
        order_page.set_name(name)
        order_page.click_surname()
        order_page.set_surname(surname)
        order_page.click_address()
        order_page.set_address(address)
        order_page.click_metro_station_choose()
        order_page.click_metro_station()
        order_page.click_phone()
        order_page.set_phone(telephone)
        order_page.click_button_next()
        order_page.wait_for_load_header_about_rent()
        order_page.click_date()
        order_page.click_day()
        order_page.click_rent_duration()
        order_page.click_option_of_list_rent_duration()
        order_page.click_scooter_color()
        order_page.click_checkbox_grey()
        order_page.click_comment()
        order_page.set_comment(comment)
        order_page.click_order_button()
        order_page.wait_for_load_order_modal_window()
        order_page.click_yes_button()
        order_page.wait_for_load_header_modal_window()
        assert "Номер заказа" in order_page.header_pop_up().text, "Заказ не оформлен"
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()