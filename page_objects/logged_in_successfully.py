from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator_element = (By.CLASS_NAME, "post-title")
    __logout_button_element = (By.XPATH,
                               '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator_element)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_button_element)
