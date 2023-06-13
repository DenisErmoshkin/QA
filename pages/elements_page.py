import time
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        output_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text
        output_email = self.element_is_present(self.locators.CREATED_EMAIL).text
        output_cur_addr = self.element_is_present(self.locators.CREATED_CURRENT_ADRESS).text
        output_per_addr = self.element_is_present(self.locators.CREATED_PERMANENT_ADRESS).text
        return output_name, output_email, output_cur_addr, output_per_addr


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        for item in item_list:
            self.go_to_element(item)
            item.click()