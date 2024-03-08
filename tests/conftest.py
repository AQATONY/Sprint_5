import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # настраиваем опции Chrome
    options = Options()
    options.headless = False  # если нужен браузер без графического интерфейса, установить в True
    # инициализируем драйвер
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site")
    # передаем управление тесту
    yield driver
    # после выполнения теста закрываем браузер
    driver.quit()
