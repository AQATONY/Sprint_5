from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainLocators
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")


class TestRegister:
    # регистрация
    def test_registration(self):
        label_name = driver.find_element(By.XPATH, MainLocators.input_name_field)
        label_name.parent.find_element(By.NAME, "name").send_keys("Anton")
        driver.find_element(By.XPATH, MainLocators.input_email_field).send_keys("anttttoongogorohov5999@yandex.ru")
        label_password = driver.find_element(By.XPATH, MainLocators.input_password_field)
        label_password.parent.find_element(By.NAME, "Пароль").send_keys("password999")
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, MainLocators.button_register)))
        driver.find_element(By.XPATH, MainLocators.button_register).click()

    # проверка редиректа на /login после регистрации
    def test_redirect_loginpage(self):
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()
