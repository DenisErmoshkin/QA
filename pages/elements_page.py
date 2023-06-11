import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Denis Ermoshkin')
        self.element_is_visible(self.locators.EMAIL).send_keys('example@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys('NewYork city DarkStreet 56')
        self.element_is_visible(self.locators.PERMANENT_ADRESS).send_keys('NewYork city SweetStreet 58')
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)
