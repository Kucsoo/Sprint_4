from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    header_main_questions = By.XPATH, ".//div[contains(text(), 'Вопросы о важном')]"
    question_field = By.ID, "accordion__heading-{}"
    answer_field = By.ID, "accordion__panel-{}"
    scooter_img = By.XPATH, ".//img[@alt='Scooter blueprint']"
    main_header = By.CLASS_NAME, "Home_Header__iJKdX"
    cookie_button = By.CLASS_NAME, "App_CookieButton__3cvqF"
