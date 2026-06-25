from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, value = 'h2')
        assert page_title.text == title

    def click_monitors(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, value = '''[onclick="byCat('monitor')"]''')
        monitor_link.click()
    
    def check_elements_count(self, count):
        monitors = self.browser.find_elements(By.CLASS_NAME, value = 'hrefch')
        assert len(monitors) == count