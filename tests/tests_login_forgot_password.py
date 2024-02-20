from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

# Клик "войти" на cтранице восстановления пароля

driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click()
sleep(3)

# проверка редиректа на /login после ВХОДА
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

# ввод логина и пароля при входе
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('antongorohow5999@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys('password999')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
sleep(3)

# проверка редиректа на главную после ВХОДА
assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

driver.quit()