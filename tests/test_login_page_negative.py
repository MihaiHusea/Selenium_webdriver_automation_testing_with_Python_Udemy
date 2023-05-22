import time

import pytest
from selenium.webdriver.common.by import By

url = "https://practicetestautomation.com/practice-test-login/"


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username,password,expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Go to the page
        driver.get(url)
        driver.maximize_window()

        # Type username incorrectUser into Username field
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys(username)

        # Type password Password123 into Password field
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button.click()

        # Verify error message is displayed
        error_message_element = driver.find_element(By.ID, 'error')
        time.sleep(2)
        assert error_message_element.is_displayed(), "Error: Is not displayed but it should be"

        # Verify error message text is "Verify error message text is "Your username is invalid"!"
        assert error_message_element.text == expected_error_message, "Error message is not expected"

    # def test_negative_user(self, driver):
    #     # Open page
    #     # Go to the page
    #     driver.get(url)
    #     driver.maximize_window()
    #
    #     # Type username incorrectUser into Username field
    #     username_input = driver.find_element(By.ID, "username")
    #     username_input.send_keys("incorrectUser")
    #
    #     # Type password Password123 into Password field
    #     password_input = driver.find_element(By.NAME, "password")
    #     password_input.send_keys("Password123")
    #
    #     # Push Submit button
    #     submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    #     submit_button.click()
    #
    #     # Verify error message is displayed
    #     error_message_element = driver.find_element(By.ID, 'error')
    #     time.sleep(3)
    #     assert error_message_element.is_displayed(), "Error: Is not displayed but it should be"
    #
    #     # Verify error message text is "Verify error message text is "Your username is invalid"!"
    #     assert error_message_element.text == "Your username is invalid!", "Error message is not expected"
    #
    # def test_negative_password(self, driver):
    #     # Open page
    #     driver.get(url)
    #     driver.maximize_window()
    #
    #     # Type username student into Username field
    #     username_input = driver.find_element(By.ID, "username")
    #     username_input.send_keys("student")
    #
    #     # Type password incorrectPassword into Password field
    #     password_input = driver.find_element(By.NAME, "password")
    #     password_input.send_keys("incorrectPassword")
    #
    #     # Push Submit button
    #     submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    #     submit_button.click()
    #
    #     # Verify error message is displayed
    #     error_message_element = driver.find_element(By.ID, 'error')
    #     time.sleep(3)
    #     assert error_message_element.is_displayed(), "Error: Is not displayed but it should be"
    #
    #     # Verify error message text is "Verify error message text is "Your username is invalid"!"
    #     assert error_message_element.text == "Your password is invalid!", "Error message is not expected"
