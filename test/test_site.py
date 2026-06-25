import time
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(browser):
    homepage = HomePage(browser)
    product_page = ProductPage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title_is('Samsung galaxy s6')

def test_open_monitors(browser):
    product_page = ProductPage(browser)
    homepage = HomePage(browser)
    homepage.open()
    product_page.click_monitors()
    time.sleep(3)
    product_page.check_elements_count(2)