from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
#ererrewrq
#Qwertyuiop[1974
#https://passport.yandex.ru/auth/add?from=cloud&origin=docs_web&retpath=https%3A%2F%2Fdocs.yandex.ru%2Fdocs%3Ftype%3Ddocx&backpath=https%3A%2F%2Fdocs.yandex.ru

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver_execute_script('argument[0].scrollIntoView();', element)