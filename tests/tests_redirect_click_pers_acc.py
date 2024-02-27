from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainLocators


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

class TestRedirect:
    # Клик на кнопку "личный кабинет" на главной странице + тест редиректа
    def test_click_button_personal_acc(self):
        driver.find_element(By.XPATH, MainLocators.button_pers_acc).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site")

        # проверка редиректа на /login после ВХОДА
    def test_redirect_on_login(self):
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()
