from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for Vinted's home page locators"""
    pop_up_overlay = (By.XPATH, "//div[@data-testid='domain-select-modal--overlay']")
    pop_up = (By.XPATH, "//div[@data-testid='domain-select-modal']")
    pop_up_close_btn = (By.XPATH, "//button[@data-testid='domain-select-modal-close-button']")
    pop_up_spain_btn = (By.XPATH, "//h2[contains(text(), 'España')]/parent::div")
    searchBar = (By.XPATH, "//input[@data-testid='search-text--input']")