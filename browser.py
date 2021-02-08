import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
load_dotenv()

class Browser(object):
    
    op = webdriver.ChromeOptions()

    if os.getenv('HEADLESS') == 'True':
        op.add_argument('headless')
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def browser_quit(self):
        self.driver.quit()

    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()