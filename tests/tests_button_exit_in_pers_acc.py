from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import MainLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


class TestAccount:

    # Клик "войти" на главной странице
    def test_login_button(self):
        driver.find_element(By.XPATH, MainLocators.button_login_mainpage).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/")

    # ввод логина и пароля при входе
    def test_login(self):
        driver.find_element(By.XPATH, MainLocators.input_email_field).send_keys(
            'anttttoongoorohov5999@yandex.ru')
        label_password = driver.find_element(By.XPATH, MainLocators.input_password_field)
        label_password.parent.find_element(By.NAME, "Пароль").send_keys("password999")
        driver.find_element(By.XPATH, MainLocators.button_log_loginpage).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/login")

    # переход в личный кабинет
    def test_redirect_personal_account(self):
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, MainLocators.button_pers_acc)))
        driver.find_element(By.XPATH, MainLocators.button_pers_acc).click()

    def test_exit_button(self):
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, MainLocators.button_exit)))
        driver.find_element(By.XPATH, MainLocators.button_exit).click()

    def test_redirect(self):
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()
