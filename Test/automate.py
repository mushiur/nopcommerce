from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import unittest
from pageObject.openBrowser import OpenBrowser
from pageObject.register import Register
from pageObject.login import Login
from pageObject.search import Search


class TestFullCycle(unittest.TestCase):

    s = Service("../Driver/chromedriver.exe")
    x = webdriver.Chrome(service=s)

    def test_1(self):
        open_browser = OpenBrowser(self.x)
        open_browser.open_webBrowser()

    def test_2(self):
        reg = Register(self.x)
        reg.registration()
        reg.gender()
        reg.name()
        reg.dob()
        reg.email()
        reg.company()
        reg.password()
        reg.Confirmpass()
        reg.RegConfirm()
        reg.Logout()

    def test_3(self):
        log = Login(self.x)
        log.log_in()
        log.log_email()
        log.log_password()
        log.confirmLog()

    def test_4(self):
        search = Search(self.x)
        search.search_box()

    if __name__ == '__main__':
        unittest.main()
