from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Открытие сайта конструктора
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

# Проверка редиректа на "начинки"
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]").click()
sleep(2)

# Поиска таба "начинки"
WebDriverWait(driver, 5).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]")))

driver.quit()
