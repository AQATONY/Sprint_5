from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import MainLocators

# Открытие сайта конструктора
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

class Testclick:
    # Проверка клика "соусы"
    def test_click_sauce(self):
        sauces = driver.find_element(By.XPATH, MainLocators.sauces_tab)
        sauces.click()
        assert "current" in sauces.get_attribute('class')


        driver.quit()