from selenium import webdriver
import pytest
from PageObject.Login import Login

class Test_Add:
    def test_new(self):
        url = "https://admin-demo.nopcommerce.com/"
        username = "admin@yourstore.com"
        password = "admin"


        driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Python 3.9\\Drivers\\chromedriver.exe")
        driver.get(url)
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys(username)
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys(password)
        driver.find_element_by_xpath("//input[@class='button-1 login-button']").click()


