import time
from selenium import webdriver

url = 'https://www.selenium.dev/'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)
