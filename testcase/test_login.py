import pytest
from selenium import webdriver
from Pageobject.LoginPage import LoginPage

class Test_001_login:
    baseURL = "https:\\admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self):
        self.driver = webdriver.chrome(
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "your store. Login":
            assert True
        else:
            assert False

