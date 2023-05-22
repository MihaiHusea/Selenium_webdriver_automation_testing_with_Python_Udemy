import pytest
from page_objects.exception_page import ExceptionPage

url = "https://practicetestautomation.com/practice-test-exceptions/"


class TestExceptions:
    @pytest.mark.PO
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.save_second_row("Sushi")
        assert exception_page.confirmation_text() == "Row 2 was saved", "Error, row 2 not saved, and should be"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.clear_row1_input()
        exception_page.save_first_row("fish and chips")
        assert exception_page.confirmation_text() == "Row 1 was saved", "Error, row 2 not saved, and should be"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert not exception_page.instructions_displayed(), "Error: instructions text should not be displayed"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row_in_3_sec()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"

