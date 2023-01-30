"""Методы для проверки ответов запросов"""
from requests import Response


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Провал! Статус код {result.status_code} не соответствует ожидаемому {status_code}"
        print("Успешно! Статус код = " + str(result.status_code))