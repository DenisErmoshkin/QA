import time
import  re
from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            # assert "Name:" + str(full_name) == str(output_name)
            assert full_name == output_name[output_name.find(':') + 1 :]
            assert email == output_email[output_email.find(':') + 1 :]
            current_address = re.sub("^\s+|\n|\r|\s+$", ' ', current_address)
            assert current_address == output_cur_addr[output_cur_addr.find(':') + 1 :]
            permanent_address = re.sub("^\s+|\n|\r|\s+$", ' ', permanent_address)
            assert permanent_address == output_per_addr[output_per_addr.find(':') + 1 :]
            # print(full_name)
            # print(email)
            # print(current_address)
            # print(permanent_address)

    class TestCheckBox:
            def test_check_box(self, driver):
                check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
                check_box_page.open()
                check_box_page.open_full_list()
                check_box_page.click_random_checkbox()
                check_box_page.get_checked_checkboxes()
                time.sleep(5)