from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from utils.price_parser import parse_price
from utils.logger import log
import time

def get_price_walmart(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)  # Allow time for JS to load

        try:
            price_element = driver.find_element(By.CLASS_NAME, "price-characteristic")
            price = float(price_element.get_attribute("content"))
            driver.quit()
            return price
        except NoSuchElementException:
            log(f"[WARN] Price element not found on Walmart page: {url}")
            driver.quit()
            return None

    except WebDriverException as e:
        log(f"[ERROR] Selenium WebDriver failed: {e}")
        return None