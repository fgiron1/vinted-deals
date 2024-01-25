from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import HomePageLocators as HP

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    
    def enter_text(self, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_Item(self, text):
        self.enter_text(HP.searchBar, text + Keys.ENTER)