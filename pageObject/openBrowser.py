class OpenBrowser:

    def __init__(self, driver):
        self.driver = driver

    def open_webBrowser(self):
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()
        print(self.driver.title)

