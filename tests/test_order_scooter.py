from pages.order_page import OrderPage
from pages.main_page import MainPageScooter
import helpers


class TestMakeOrder:
    driver = None

    def test_make_order_header_button_without_comment_success(self, driver):
        main_page = MainPageScooter(driver)
        order_page = OrderPage(driver)
        main_page.click_header_order_button()
        order_page.wait_for_load_header_for_whom_scooter()
        order_page.set_order_conditions_for_whom_scooter(helpers.random_name(), helpers.random_surname(),
                                                helpers.random_address(), helpers.random_telephone())
        order_page.set_order_conditions_about_rent_comment_no()
        assert "Номер заказа" in order_page.header_pop_up().text, "Заказ не оформлен"

    def test_make_order_main_page_button_with_comment_success(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPageScooter(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_order_button()
        main_page.click_order_button()
        order_page.wait_for_load_header_for_whom_scooter()
        order_page.set_order_conditions_for_whom_scooter(helpers.random_name(), helpers.random_surname(),
                                                helpers.random_address(), helpers.random_telephone())
        order_page.set_order_conditions_about_rent_comment_yes(helpers.random_comment())
        assert "Номер заказа" in order_page.header_pop_up().text, "Заказ не оформлен"
