from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# вход в личный кабинет
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('antongorohow5999@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys('password999')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
sleep(3)


# Клик на "личный кабинет"
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
sleep(3)

# Клик на кнопку "выход" в личном кабинете
driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button").click()
sleep(3)

# проверка редиректа на страницу авторизации после выхода из аккаунта
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.quit()