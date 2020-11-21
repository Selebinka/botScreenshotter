import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_screenshot_from_page(url: str, screenshot_path: str):
    """Get and save screenshot"""
    driver = _get_webdriver()
    driver.get(url)
    el = _set_full_page_size(driver).find_element_by_tag_name('body')
    el.screenshot(screenshot_path)
    driver.quit()


def _get_webdriver() -> webdriver:
    """Return webdriver instance"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


def _set_full_page_size(driver):
    """Scroll page to max height"""
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)
    return driver
