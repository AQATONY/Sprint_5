from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# регистрация
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('Anton')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(
    'antongorohov5999@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys('password999')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
sleep(10)

# проверка редиректа на /login после регистрации
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.quit()
