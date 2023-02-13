"""Methods for Checking Query Responses"""
import json

import allure


class Checking():

    """Method for checking code status"""

    @staticmethod
    @allure.step
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Failure! Status code {result.status_code} does not match the expected {status_code}"
        print("Successfully! Status code = " + str(result.status_code))


    """Method for checking the presence of required fields in the request response"""

    @staticmethod
    @allure.step
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value, f"Fields in the response {list(token)} do not match the expected {expected_value}"
        print("All fields are present")


    """Method for checking the values of required fields in the request response"""

    @staticmethod
    @allure.step
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Status field value - {check_info} does not match the expected value {expected_value}"
        print(field_name + " true!")