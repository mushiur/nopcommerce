import TestData.searchData


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search_box(self):
        element = self.driver.find_element("id", "small-searchterms")
        element.click()
        element.send_keys(TestData.searchData.productName)
        element.submit()
