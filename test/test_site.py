import time
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

def test_open_monitors(browser):
    browser.get('https://demoblaze.com/index.html')
    monitor_link = browser.find_element(By.CSS_SELECTOR, value = '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(3)
    monitors = browser.find_elements(By.CLASS_NAME, value = 'hrefch')
    assert len(monitors) == 2