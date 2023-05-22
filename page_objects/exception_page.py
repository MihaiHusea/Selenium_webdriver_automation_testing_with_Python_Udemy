from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, 'add_btn')
    __save_button_row1 = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __save_button_row2 = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __edit_button_row1 = (By.XPATH, "//div[@id='row1']/button[@name='Edit']")
    __input_field_row1_locator = (By.XPATH, "//div[@id='row1']/input")
    __input_field_row2_locator = (By.XPATH, "//div[@id='row2']/input")
    __confirmation_locator = (By.ID, 'confirmation')
    __instructions_locator = (By.ID, 'instructions')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__input_field_row2_locator)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__input_field_row2_locator)

    def save_second_row(self, text: str):
        super()._type(self.__input_field_row2_locator, text)
        super()._click(self.__save_button_row2)
        super()._wait_until_element_is_visible(self.__confirmation_locator)

    def confirmation_text(self):
        return super()._get_text(self.__confirmation_locator)

    def clear_row1_input(self):
        super()._click(self.__edit_button_row1)
        super()._wait_until_element_is_clickable(self.__input_field_row1_locator)
        super()._clear(self.__input_field_row1_locator)

    def save_first_row(self, text: str):
        super()._type(self.__input_field_row1_locator, text)
        super()._click(self.__save_button_row1)
        super()._wait_until_element_is_visible(self.__confirmation_locator)

    def instructions_displayed(self):
        super()._is_displayed(self.__instructions_locator)

    def add_second_row_in_3_sec(self, time: int = 3):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__input_field_row2_locator, time)
