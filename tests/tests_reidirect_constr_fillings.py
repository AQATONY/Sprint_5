from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import MainLocators
import pytest



@pytest.fixture
class TestClick:
    # Проверка клика на "начинки"
    def test_click_tab_fillings(driver):
        fillings = driver.find_element(By.XPATH, MainLocators.fillings_tab)
        fillings.click()
        assert "current" in fillings.get_attribute('class')


