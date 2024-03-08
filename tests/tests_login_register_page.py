from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainLocators

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

class TestAccount:
    # Клик "войти" на cтранице регистрации
    def test_click_login(self):
        driver.find_element(By.XPATH, MainLocators.button_blue_login).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/register")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    # ввод логина и пароля при входе
    def test_login_password(self):
        driver.find_element(By.XPATH, MainLocators.input_email_field).send_keys(
            'anttttoongoorohov5999@yandex.ru')
        label_password = driver.find_element(By.XPATH, MainLocators.input_password_field)
        label_password.parent.find_element(By.NAME, "Пароль").send_keys("password999")
        driver.find_element(By.XPATH, MainLocators.button_log_loginpage).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/login")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        driver.quit()
