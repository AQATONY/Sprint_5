from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainLocators



# Открытие страницы регистрации
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")


class TestRegistrarionShortPass:
    def test_short_pass_reg(self):
        # регистрация с коротким паролем
        label_name = driver.find_element(By.XPATH, MainLocators.input_name_field)
        label_name.parent.find_element(By.NAME, "name").send_keys("Anton")
        driver.find_element(By.XPATH, MainLocators.input_email_field).send_keys("antotonngoorohov5999@yandex.ru")
        label_password = driver.find_element(By.XPATH, MainLocators.input_password_field)
        label_password.parent.find_element(By.NAME, "Пароль").send_keys("123")
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, MainLocators.button_register)))
        driver.find_element(By.XPATH, MainLocators.button_register).click()
        # Проверка алерта о неправильном пароле
        show_alert = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, MainLocators.wrong_pass_alert)))
        assert show_alert.text == "Некорректный пароль"

        driver.quit()
