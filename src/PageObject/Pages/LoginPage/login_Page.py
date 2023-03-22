from selenium import webdriver
from selenium.webdriver.common.by import By
from src.PageObject.Pages.Locators import OpenSource_ALl_Locators

class Login_Page(object):
    def __init__(self, driver):
        self.driver = driver


    def input_username(self, username):
        self.driver.find_element(By.NAME, OpenSource_ALl_Locators.username_name).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.NAME, OpenSource_ALl_Locators.pass_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.TAG_NAME, OpenSource_ALl_Locators.login_tagname).click()

    def click_logout_option(self):
        self.driver.find_element(By.CSS_SELECTOR, OpenSource_ALl_Locators.click_logout_option_CSS).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, OpenSource_ALl_Locators.logout_XPath).click()



