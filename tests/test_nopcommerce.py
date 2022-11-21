from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import unittest
from pageObject.openBrowser import OpenBrowser
from pageObject.register import Register
from pageObject.login import Login
from pageObject.search import Search
from pageObject.shoppingCart import ShoppingCart
from pageObject.checkout import CheckOut


class TestFullCycle(unittest.TestCase):
    s = Service("../driver/chromedriver.exe")
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
        reg.confirmPass()
        reg.regConfirm()
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
        search.choose_product()

    def test_5(self):
        cart = ShoppingCart(self.x)
        cart.enter_text()
        cart.add_cart()
        cart.shopping_cart()

    def test_6(self):
        check_out = CheckOut(self.x)
        check_out.checkout_button()
        check_out.billing_page()
        check_out.checkout_page()

    if __name__ == '__main__':
        unittest.main()
