import time
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name[output_name.find(':') + 1 :]
            assert email == output_email[output_email.find(':') + 1 :]
            assert current_address == output_cur_addr[output_cur_addr.find(':') + 1 :]
            assert permanent_address == output_per_addr[output_per_addr.find(':') + 1 :]
            # print(output_name.replace('Name:', ''))
            # print(output_name[output_name.find(':') + 1 :])
            # assert permanent_address[: permanent_address.find('/')] + " " + permanent_address[permanent_address.find('n') + 1 :] == 0
            # print(output_per_addr[output_per_addr.find(':') + 1 :])
            # print(current_address)
            # print(permanent_address)
            # print(output_name, output_email, output_cur_addr, output_per_addr)