import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "https://practicetestautomation.com/practice-test-exceptions/"


class TestExceptions:
    # @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get(url)
        driver.maximize_window()

        # Click add button
        add_button = driver.find_element(By.ID, 'add_btn')
        add_button.click()

        # Verify Row2 input field is displayed
        wait = WebDriverWait(driver=driver, timeout=10)
        input_field_row_2_element = wait.until(ec.presence_of_element_located((By.ID, 'row2')))
        # input_field_row_2 = driver.find_element(By.ID, 'row2')
        assert input_field_row_2_element._is_displayed(), "Row 2 input should be displayed, but it's not"

    # @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get(url)
        driver.maximize_window()
        # Click add button
        add_button = driver.find_element(By.ID, 'add_btn')
        add_button.click()
        # find input element row2 and wait to load
        wait = WebDriverWait(driver=driver, timeout=10)
        input_field_row_2_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # type text into the second input field
        input_field_row_2_element.send_keys("fish and chips")
        # save text in row2
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()
        # verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, 'confirmation')))
        assert confirmation_element.text == "Row 2 was saved", "Error, row 2 not saved, and should be"

    # @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get(url)
        driver.maximize_window()
        # Clear input field
        driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Edit']").click()
        row_1_input_field_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver=driver, timeout=10)
        wait.until(ec.element_to_be_clickable(row_1_input_field_element))
        row_1_input_field_element.clear()

        # Type text into input field
        row_1_input_field_element.send_keys("Sushi")
        driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']").click()

        # Verify text changed
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, 'confirmation')))
        assert confirmation_element.text == "Row 1 was saved", "Error, row 2 not saved, and should be"

    # @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)

        # Find the instructions text element
        instructions_element = driver.find_element(By.ID, 'instructions')

        # Push add button
        add_button = driver.find_element(By.XPATH, '//div[@id="row1"]/button[@name="Add"]')
        add_button.click()
        time.sleep(1)

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver=driver, timeout=10)

        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, 'instructions')), "Error: instructions text element should not be displayed")

    # @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get(url)
        driver.maximize_window()

        # Click Add button
        add_button = driver.find_element(By.XPATH, '//div[@id="row1"]/button[@name="Add"]')
        add_button.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver=driver, timeout=6)
        second_input_field_element = wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="row2"]/input')),
                                                "Failed waiting for row 2 input to be visible")

        # Verify second input field is displayed
        assert second_input_field_element._is_displayed(), "Error: Element is not displayed"
