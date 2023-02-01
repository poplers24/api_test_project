import datetime
import os


class Logger():
    # называем файл
    file_name = "logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        # открываем файл
        with open(cls.file_name, 'a', encoding="utf-8") as logger_file:
            # и записываем в файл
            logger_file.write(data)

    # Метод получения данных по запросу
    @classmethod
    def add_request(cls, url: str, method: str):
        # переменная с помощью которой помещаем в лог название теста который в даный момент выполняется
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # формируем строки по запросу
        data_to_add = "\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        # записываем данные в файл
        cls.write_log_to_file(data_to_add)

    # Метод получения данных по ответу
    @classmethod
    # result - результат запроса в http_method
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        # формируем строки по ответу
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += "\n-----\n"

        # записываем данные в файл
        cls.write_log_to_file(data_to_add)

