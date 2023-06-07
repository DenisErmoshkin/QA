import pytest
from selenium import webdriver


@pytest.fixture(scope='function')

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
"""
Этот код представляет собой фикстуру Pytest, которая создает и настраивает экземпляр драйвера Chrome 
для автоматизации тестирования веб-приложений. Фикстура имеет область видимости 'function', что означает, 
что она будет выполняться для каждой функции теста отдельно.
"""