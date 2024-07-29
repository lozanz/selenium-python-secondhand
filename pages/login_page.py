from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.masuk_button = (By.XPATH, "//a[contains(.,'Masuk')]")
        self.email_input = (By.ID, 'user_email')
        self.password_input = (By.ID, 'user_password')
        self.login_button = (By.XPATH, "//input[@name='commit']")

    def click_masuk(self):
        self.driver.find_element(*self.masuk_button).click()
        
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
