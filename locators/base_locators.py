from selenium.webdriver.common.by import By
class BaseLocators:
    logo_yandex = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    logo_scooter = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
    order_button = By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[@class = 'Button_Button__ra12g']"
    enter_button = By.XPATH, ".//button[@aria-label='Войти']"