import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def setup_browser():
    options = Options ()
    options.add_argument('--headless')
    # options.headless = True
    pytest.driver = webdriver.Chrome(options=options)
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.set_window_size(1452, 924)
    pytest.driver.set_window_position(-7, -3)

    yield  # pytest.driver

    pytest.driver.quit()

# pytest -v --driver Chrome --driver-path D:/WebDriver/chromedriver.exe tests/test_petFriends.py
# pytest -v --driver Chrome tests/test_petFriends.py