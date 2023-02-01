"""Методы для проверки ответов запросов"""
import json

import allure


class Checking():

    """Метод для проверки статус кода"""


    @staticmethod
    @allure.step
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Провал! Статус код {result.status_code} не соответствует ожидаемому {status_code}"
        print("Успешно! Статус код = " + str(result.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""


    @staticmethod
    @allure.step
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value, f"Поля в ответе {list(token)} не соответствуют ожидаемым {expected_value}"
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""


    @staticmethod
    @allure.step
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Значение поля status - {check_info} не соответствует ожидаемому значению {expected_value}"
        print(field_name + " верен!")