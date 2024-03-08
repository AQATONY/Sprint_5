from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import MainLocators
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")


class TestAccount:
    def test_login_pers_acc(self):
        driver.find_element(By.XPATH, MainLocators.input_email_field).send_keys(
            'anttttoongoorohov5999@yandex.ru')
        label_password = driver.find_element(By.XPATH, MainLocators.input_password_field)
        label_password.parent.find_element(By.NAME, "Пароль").send_keys("password999")
        driver.find_element(By.XPATH, MainLocators.button_log_loginpage).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/login")

    def test_click_pers_acc(self):
        # Клик на "личный кабинет"
        driver.find_element(By.XPATH, MainLocators.button_pers_acc).click()

    def test_click_button_contructon(self):
        # Клик на кнопку "конструктор" в личном кабинете
        driver.find_element(By.XPATH, MainLocators.button_constr).click()

    def test_redirect_on_mainpage(self):
        # проверка редиректа на главную, то есть на окно конструктора
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        driver.quit()
