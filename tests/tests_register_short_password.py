from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# регистрация с коротким паролем
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('Anton')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(
    'antongorohov5999@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys('1234')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()



# Ожидание алерта о неправильном пароле
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")))

driver.quit()