import datetime
import os


class Logger():
    # name the file
    file_name = "logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        # open file
        with open(cls.file_name, 'a', encoding="utf-8") as logger_file:
            # and write to file
            logger_file.write(data)

    # method of obtaining data on request
    @classmethod
    def add_request(cls, url: str, method: str):
        # a variable with which we put in the log the name of the test that is currently being executed
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # form strings on request
        data_to_add = "\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        # write data to file
        cls.write_log_to_file(data_to_add)

    # response data retrieval method
    @classmethod
    # result - query result in http_method
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        # form strings according to the answer
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += "\n-----\n"

        # write data to file
        cls.write_log_to_file(data_to_add)

