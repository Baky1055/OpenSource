import time

import unittest

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.LoginPage.login_Page import Login_Page
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# valid username & password
valid_username = "Admin"
valid_password = "admin123"

# invalid username & password
invalid_username = "abcde"
invalid_password = "abchj123"

# Blank username and Pass
blank_username = ' '
blank_password = ' '




class test_login_page(WebDriverSetup):

    def test_log_in_page(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        log_in_page = Login_Page(driver)
        log_in_page.input_username(valid_username)
        log_in_page.input_password(valid_password)
        log_in_page.click_login_button()


    def test_sign_in_with_valid_user_and_pass(self):
        driver = self.driver
        data = {
            "email" : valid_username,
            "password" : valid_password
        }
        signin_helper_valid_user_and_pass(driver,data)
        try:
            signout_helper(driver)
        except NoSuchElementException:
            self.fail('Not ok')

    def test_sign_in_valid_user_and_invalid_pass(self):
        driver = self.driver
        data = {
            "email" : valid_username,
            "password" : invalid_password
        }
        signin_helper_valid_user_and_pass(driver,data)
        try:
            signout_helper(driver)
            self.fail()
        except NoSuchElementException:
            pass

    def test_sign_in_with_invalid_user_and_valid_pass(self):
        driver = self.driver
        data = {
            "email" : invalid_username,
            "password" : valid_password
        }
        signin_helper_valid_user_and_pass(driver,data)
        try:
            signout_helper(driver)
            self.fail()
        except NoSuchElementException:
            pass




def signin_helper_valid_user_and_pass(driver, row):
    driver.delete_all_cookies()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    try:
        log_in_page = Login_Page(driver)
        log_in_page.input_username(row['email'])
        log_in_page.input_password(row['password'])
        log_in_page.click_login_button()
        time.sleep(1)

    except NoSuchElementException:
        return 0

def signout_helper(driver):
    logout_Option = driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name")
    logout_Option.click()
    time.sleep(3)

    logout = logout_Option.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    logout.click()

if __name__ == '__main__':
    unittest.main()


