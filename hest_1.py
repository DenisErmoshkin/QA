import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def quest():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options=chrome_options)

    url = 'https://passport.yandex.ru/auth/add?from=cloud&origin=docs_web&retpath=https%3A%2F%2Fdocs.yandex.ru%2Fdocs%3Ftype%3Ddocx&backpath=https%3A%2F%2Fdocs.yandex.ru'
    driver = webdriver.Chrome()
    driver.get(url)


    qwe = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
    qwe.send_keys('ererrewrq')
    qwe.send_keys(Keys.ENTER)

    time.sleep(1)

    qwe1 = driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
    qwe1.send_keys('Qwertyuiop[1974')
    qwe1.send_keys(Keys.ENTER)

    time.sleep(7)

    qwe2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/a[1]')
    qwe2.click()
    qwe3 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/div/ul/div[1]/div/span')

    if qwe3.text == 'ererrewrq':
        asd = 'TEST "LOGIN" WAS PASSED'
    else:
        asd = 'TEST "LOGIN" WAS NOT PASSED'

    time.sleep(3)

    return asd, qwe3.text

a = quest()
print(a)