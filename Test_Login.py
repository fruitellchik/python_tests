# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_login(self):
        wd = self.wd
        wd.get("https://fix-online.sbis.ru/auth/?ret=%2F")
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys("admin148")
        wd.find_element_by_name("password").click()
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin1488")
        wd.find_element_by_xpath("//body[@id='body']/div/div/div[7]/div/div/div/div[2]/span/div/div/a[5]/span[3]").click()
        wd.find_element_by_xpath("//div[2]/div/a/span/span").click()
        wd.find_element_by_xpath("//div[@id='popup']/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
        def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
