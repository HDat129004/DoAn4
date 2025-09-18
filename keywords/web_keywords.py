class WebKeywords:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, locator, expected):
        actual = self.driver.find_element(*locator).text
        assert expected in actual, f"Expected '{expected}' but got '{actual}'"
