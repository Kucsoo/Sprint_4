from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def header_pop_up(self):
        return self.driver.find_element(*OrderPageLocators.header_modal_window)

    def click_name(self):
        element = self.driver.find_element(*OrderPageLocators.name_input)
        self.click(element)
    def set_name(self, name):
        element = self.driver.find_element(*OrderPageLocators.name_input)
        self.send_keys(element, name)

    def click_surname(self):
        element = self.driver.find_element(*OrderPageLocators.surname_input)
        self.click(element)

    def set_surname(self, surname):
        element = self.driver.find_element(*OrderPageLocators.surname_input)
        self.send_keys(element, surname)

    def click_address(self):
        element = self.driver.find_element(*OrderPageLocators.address_input)
        self.click(element)

    def set_address(self, address):
        element = self.driver.find_element(*OrderPageLocators.address_input)
        self.send_keys(element, address)

    def click_metro_station_choose(self):
        element = self.driver.find_element(*OrderPageLocators.metro_station_choose)
        self.click(element)

    def click_list_of_metro_stations(self):
        element = self.driver.find_element(*OrderPageLocators.list_metro)
        self.click(element)

    def click_metro_station(self):
        element = self.driver.find_element(*OrderPageLocators.metro_station)
        self.click(element)

    def click_phone(self):
        element = self.driver.find_element(*OrderPageLocators.phone_number_input)
        self.click(element)

    def set_phone(self, telephone):
        element = self.driver.find_element(*OrderPageLocators.phone_number_input)
        self.send_keys(element, telephone)

    def click_button_next(self):
        element = self.driver.find_element(*OrderPageLocators.button_next)
        self.click(element)

    def click_order_button(self):
        element = self.driver.find_element(*OrderPageLocators.order_button)
        self.click(element)

    def click_date(self):
        element = self.driver.find_element(*OrderPageLocators.date_input)
        self.click(element)

    def click_day (self):
        element = self.driver.find_element(*OrderPageLocators.day_in_calendar)
        self.click(element)

    def click_rent_duration(self):
        element = self.driver.find_element(*OrderPageLocators.rent_duration)
        self.click(element)


    def click_option_of_list_rent_duration(self):
        element = self.driver.find_element(*OrderPageLocators.option_of_list_rent_duration)
        self.click(element)

    def click_scooter_color(self):
        element = self.driver.find_element(*OrderPageLocators.scooter_color_input)
        self.click(element)

    def click_checkbox_black(self):
        element = self.driver.find_element(*OrderPageLocators.checkbox_black)
        self.click(element)

    def click_checkbox_grey(self):
        element = self.driver.find_element(*OrderPageLocators.checkbox_grey)
        self.click(element)

    def click_comment(self):
        element = self.driver.find_element(*OrderPageLocators.comment_input)
        self.click(element)

    def set_comment(self, comment):
        element = self.driver.find_element(*OrderPageLocators.comment_input)
        self.send_keys(element, comment)

    def click_yes_button(self):
        element = self.driver.find_element(*OrderPageLocators.yes_button)
        self.click(element)

    def wait_for_load_header_for_whom_scooter(self):
        self.wait_element(OrderPageLocators.order_header_for_whom_scooter)

    def wait_for_load_header_about_rent(self):
        self.wait_element(OrderPageLocators.header_about_rent)

    def wait_for_load_order_modal_window(self):
        self.wait_element(OrderPageLocators.order_modal_window)

    def wait_for_load_header_modal_window(self):
        self.wait_element(OrderPageLocators.header_modal_window)

    def set_order_conditions_for_whom_scooter(self, name, surname, address, telephone):
        self.click_name()
        self.set_name(name)
        self.click_surname()
        self.set_surname(surname)
        self.click_address()
        self.set_address(address)
        self.click_metro_station_choose()
        self.click_metro_station()
        self.click_phone()
        self.set_phone(telephone)
        self.click_button_next()
        self.wait_for_load_header_about_rent()

    def set_order_conditions_about_rent_comment_yes(self, comment):
        self.click_date()
        self.click_day()
        self.click_rent_duration()
        self.click_option_of_list_rent_duration()
        self.click_scooter_color()
        self.click_checkbox_grey()
        self.click_comment()
        self.set_comment(comment)
        self.click_order_button()
        self.wait_for_load_order_modal_window()
        self.click_yes_button()
        self.wait_for_load_header_modal_window()

    def set_order_conditions_about_rent_comment_no(self):
        self.click_date()
        self.click_day()
        self.click_rent_duration()
        self.click_option_of_list_rent_duration()
        self.click_scooter_color()
        self.click_checkbox_grey()
        self.click_order_button()
        self.wait_for_load_order_modal_window()
        self.click_yes_button()
        self.wait_for_load_header_modal_window()
