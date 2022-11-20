import testData.searchData


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search_box(self):
        element = self.driver.find_element("id", "small-searchterms")
        element.click()
        element.send_keys(testData.searchData.productName)
        element.submit()

    def choose_product(self):
        self.driver.find_element("xpath", "//a[normalize-space()='Custom T-Shirt']").click()

