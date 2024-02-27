from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainLocators

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")


class TestAccount:
    # Клик "войти" на cтранице восстановления пароля + проверка редиректа
    def test_click_login(self):
        driver.find_element(By.XPATH, MainLocators.button_blue_login).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/forgot-password")

    # проверка перехода на /login после ВХОДА
    def test_redirect_login(self):
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    # ввод логина и пароля при входе + проверка редиректа
    def test_login(self):
        driver.find_element(By.XPATH, MainLocators.input_email_field).send_keys(
            'anttttoongoorohov5999@yandex.ru')
        label_password = driver.find_element(By.XPATH, MainLocators.input_password_field)
        label_password.parent.find_element(By.NAME, "Пароль").send_keys("password999")
        driver.find_element(By.XPATH, MainLocators.button_log_loginpage).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/login")

    # проверка перехода на главную после ВХОДА
    def test_redirect_main_page(self):
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        driver.quit()
