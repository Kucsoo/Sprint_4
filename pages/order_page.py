from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def header_for_whom_scooter(self):
        return self.driver.find_element(*OrderPageLocators.order_header_for_whom_scooter)

    def name(self):
        return self.driver.find_element(*OrderPageLocators.name_input)

    def surname(self):
        return self.driver.find_element(*OrderPageLocators.surname_input)

    def address(self):
        return self.driver.find_element(*OrderPageLocators.address_input)

    def metro_station_choose(self):
        return self.driver.find_element(*OrderPageLocators.metro_station_choose)

    def list_of_metro_stations(self):
        return self.driver.find_element(*OrderPageLocators.list_metro)

    def metro_station(self):
        return self.driver.find_element(*OrderPageLocators.metro_station)

    def phone(self):
        return self.driver.find_element(*OrderPageLocators.phone_number_input)

    def button_next(self):
        return self.driver.find_element(*OrderPageLocators.button_next)

    def button_back(self):
        return self.driver.find_element(*OrderPageLocators.button_back)

    def order_button(self):
        return self.driver.find_element(*OrderPageLocators.order_button)

    def header_rent(self):
        return self.driver.find_element(*OrderPageLocators.header_about_rent)

    def date(self):
        return self.driver.find_element(*OrderPageLocators.date_input)

    def day (self):
        return self.driver.find_element(*OrderPageLocators.day_in_calendar)

    def rent_duration(self):
        return self.driver.find_element(*OrderPageLocators.rent_duration)

    def list_rent_duration(self):
        return self.driver.find_element(*OrderPageLocators.list_rent_duration)

    def option_of_list_rent_duration(self):
        return self.driver.find_element(*OrderPageLocators.option_of_list_rent_duration)

    def scooter_color(self):
        return self.driver.find_element(*OrderPageLocators.scooter_color_input)

    def checkbox_black(self):
        return self.driver.find_element(*OrderPageLocators.checkbox_black)

    def checkbox_grey(self):
        return self.driver.find_element(*OrderPageLocators.checkbox_grey)

    def comment(self):
        return self.driver.find_element(*OrderPageLocators.comment_input)

    def order_pop_up(self):
        return self.driver.find_element(*OrderPageLocators.order_modal_window)

    def yes_button(self):
        return self.driver.find_element(*OrderPageLocators.yes_button)

    def header_pop_up(self):
        return self.driver.find_element(*OrderPageLocators.header_modal_window)
    def click_name(self):
        self.name().click()
    def set_name(self, name):
        self.name().send_keys(name)
    def click_surname(self):
        self.surname().click()

    def set_surname(self, surname):
        self.surname().send_keys(surname)

    def click_address(self):
        self.address().click()

    def set_address(self, address):
        self.address().send_keys(address)

    def click_metro_station_choose(self):
        self.metro_station_choose().click()

    def click_list_of_metro_stations(self):
        self.list_of_metro_stations().click()
    def click_metro_station(self):
        self.metro_station().click()

    def click_phone(self):
        self.phone().click()
    def set_phone(self, telephone):
        self.phone().send_keys(telephone)

    def click_button_next(self):
        self.button_next().click()
    def click_order_button(self):
        self.order_button().click()

    def click_date(self):
        self.date().click()

    def click_day (self):
        self.day().click()

    def click_rent_duration(self):
        self.rent_duration().click()


    def click_option_of_list_rent_duration(self):
        self.option_of_list_rent_duration().click()

    def click_scooter_color(self):
        self.scooter_color().click()

    def click_checkbox_black(self):
        self.checkbox_black().click()

    def click_checkbox_grey(self):
        self.checkbox_grey().click()

    def click_comment(self):
        self.comment().click()

    def set_comment(self, comment):
        self.comment().send_keys(comment)

    def click_yes_button(self):
        self.yes_button().click()

    def wait_for_load_header_for_whom_scooter(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.order_header_for_whom_scooter)))

    def wait_for_load_header_about_rent(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.header_about_rent)))

    def wait_for_load_order_modal_window(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.order_modal_window)))
    def wait_for_load_header_modal_window(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.header_modal_window)))