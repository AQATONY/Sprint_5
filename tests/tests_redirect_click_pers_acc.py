from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

# Клик на кнопку "личный кабинет" на главной странице

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
sleep(3)

# проверка редиректа на /login после ВХОДА
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.quit()
