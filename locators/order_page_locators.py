from selenium.webdriver.common.by import By
class OrderPageLocators:
    order_header_for_whom_scooter = By.XPATH,".//div[@class ='Order_Header__BZXOb']"
    name_input = By.XPATH, ".//input[@placeholder='* Имя']"
    surname_input = By.XPATH, ".//input[@placeholder='* Фамилия']"
    address_input = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    metro_station_choose = By.XPATH, ".//input[@placeholder='* Станция метро']"
    list_metro = By.XPATH, ".//ul[@class='select-search__options']"
    metro_station = By.XPATH, ".//li[@class='select-search__row' and @data-value='2']"
    phone_number_input = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    button_next = By.XPATH, ".//button [contains(text(), 'Далее')]"
    button_back = By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i'
    order_button = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    header_about_rent = By.XPATH,".//div[@class ='Order_Header__BZXOb']"
    date_input = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    day_in_calendar = By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--024']"
    rent_duration = By.CLASS_NAME, 'Dropdown-root'
    list_rent_duration = By.CLASS_NAME, 'Dropdown-menu'
    option_of_list_rent_duration = By.XPATH, ".//div[@class='Dropdown-option' and text()= 'сутки']"
    scooter_color_input = By.CLASS_NAME, 'Order_Title__3EKne'
    checkbox_black = By.ID, 'black'
    checkbox_grey = By.ID, 'grey'
    comment_input = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    order_modal_window = By.CLASS_NAME, 'Order_Modal__YZ-d3'
    yes_button = By.XPATH, ".//button[text()= 'Да']"
    header_modal_window = By.CLASS_NAME, 'Order_Text__2broi'
