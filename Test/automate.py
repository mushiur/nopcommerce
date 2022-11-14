import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

s = Service("..\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

