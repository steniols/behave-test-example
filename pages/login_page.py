from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LoginPageLocator(object):
    INPUT_USERNAME = '#frmLogin [id="txtUsername"]'
    INPUT_PASSWORD = '#frmLogin [id="txtPassword"]'
    BUTTON_LOGIN = '#frmLogin [id="btnLogin"]'
    RESULT_TEXT = "#content > div > div.head > h1"


class LoginPage(Browser):
    def __init__(self):
        self.iframe = None

    def get_element(self, locator, iframe=None):
        # if self.iframe:
        #     self.driver.switch_to_frame(iframe)
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, locator))
        )
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        # if self.iframe:
        #     self.driver.switch_to_default_content()

        return element

    def get_element_frame(self, locator):
        self.driver.switch_to_frame("rightMenu")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, locator))
        )
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        self.driver.get(url)

    def send_keys_input_user(self):
        input_user = self.get_element(LoginPageLocator.INPUT_USERNAME)
        input_user.send_keys("Admin")

    def send_keys_input_password(self):
        input_password = self.get_element(LoginPageLocator.INPUT_PASSWORD)
        input_password.send_keys("admin123")

    def click_button_login(self):
        button = self.get_element(LoginPageLocator.BUTTON_LOGIN)
        button.click()

    def get_result_text(self):
        element = self.get_element(LoginPageLocator.RESULT_TEXT)
        return element.text
