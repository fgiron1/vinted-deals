from selenium import webdriver
import os

class Base:
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(f"{os.getcwd()}/py/selenium/drivers/gecko/geckodriver.exe", options)
        # TODO: Customize browser options and flags
