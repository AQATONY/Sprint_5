from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import MainLocators

# Открытие сайта конструктора
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")


class TestClick:
    # Проверка клика на "начинки"
    def test_click_tab_fillings(self):
        fillings = driver.find_element(By.XPATH, MainLocators.fillings_tab)
        fillings.click()
        assert "current" in fillings.get_attribute('class')

        driver.quit()
