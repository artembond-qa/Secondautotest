import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dotenv
dotenv.load_dotenv()



@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Автоматически скачивает и использует правильный ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.implicitly_wait(5)
    login = driver.find_element(By.LINK_TEXT, 'Log in')
    login.click()


def test_login_works(driver):
    login(driver)

    username = os.getenv('MY_LOGIN')
    password = os.getenv('MY_PASSWORD')

    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)

    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome Test1556")
    )

    assert "Welcome Test1556" in driver.find_element(By.ID, "nameofuser").text
    print("✅ Успешный вход под Test1556!")
