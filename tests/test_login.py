from selenium import webdriver
from pages.login_page import LoginPage
from tests.data import Data
import pytest

@pytest.fixture
def browser():
    # Inisialisasi WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    options.add_experimental_option("excludeSwitches",['enable-logging'])  
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()  
    yield driver
    # Menutup browser setelah selesai pengujian
    driver.quit()    
    
@pytest.mark.parametrize("account",Data.accounts)
def test_login(browser,account):
    browser.get(Data.url)
    login_page = LoginPage(browser)
    login_page.click_masuk()
    login_page.enter_email(account['email'])
    login_page.enter_password(account['password'])
    login_page.click_login()
    
    # assert "Invalid Email or password." in browser.title
    
    