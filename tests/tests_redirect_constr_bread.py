from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import MainLocators

# Открытие сайта конструктора
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

class Testclick:
    # Проверка клика "соусы" (т.к. "булки" открыты по умолчанию)
    def test_click_on_sauce(self):
        sauces = driver.find_element(By.XPATH, MainLocators.sauces_tab)
        sauces.click()
        assert "current" in sauces.get_attribute('class')

    # Проверка клика "булки"
    def test_click_on_bread(self):
        bread = driver.find_element(By.XPATH, MainLocators.bread_tab)
        bread.click()
        assert "current" in bread.get_attribute('class')

        driver.quit()
