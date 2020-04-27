# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLoginLogout(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_login_logout(self):
        wd = self.wd
        wd.get("http://127.0.0.1/")
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("admin")
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("admin")
        wd.find_element_by_link_text(u"Войти").click()
        wd.find_element_by_xpath("//div[@id='headContainer']/a/p/i").click()
    
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