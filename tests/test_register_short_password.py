from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# регистрация с коротким паролем
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('Anton')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(
    'aaa4ddnddtdod4n5999@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys('1234')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

# поиск алерта с ошибкой "некорректный пароль"
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")

driver.quit()

