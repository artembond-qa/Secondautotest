import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dotenv
dotenv.load_dotenv()



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver

def login(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.implicitly_wait(5)
    login = driver.find_element(By.LINK_TEXT, 'Log in')
    login.click()


def test_login_works(driver):
    login(driver)
    username = os.getenv('MY_LOGIN')
    password = os.getenv('MY_PASSWORD')
    # твоя функция

    # Вводим логин и пароль (рабочие данные для demoblaze)
    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)

    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    wait = WebDriverWait(driver, 10)
    welcome_text = wait.until(
        EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome Test1556")
    )

    assert "Welcome Test1556" in driver.find_element(By.ID, "nameofuser").text
    print("✅ Успешный вход под Test1556!")
