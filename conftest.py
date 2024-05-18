import allure
import pytest
from selenium import webdriver
from data import DataTest



@pytest.fixture(scope='function', params=['chrome', 'firefox'])
@allure.title('Запуск драйвера')
def driver(request):
    if 'firefox' in request.param:
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(options=options)
        driver.get(DataTest.main_page)


    elif 'chrome' in request.param:

        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)
        driver.get(DataTest.main_page)

    yield driver

    driver.quit()

