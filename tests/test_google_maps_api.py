import json
from utils.api import Google_maps_api
from utils.checking import Checking
import allure

"""Creating, editing and deleting a new location"""

@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("\nМетод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("\nМетод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\nМетод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("\nМетод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("\nМетод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("\nTesting of creating, modifying and deleting a new location was successful\n")

    @allure.description("Test get operation failed, invalid place_id")
    def test_get_operation_failed(self):

        print("\nМетод GET 404")
        result_get = Google_maps_api.get_new_place("f8e058584c3dc7ae3d74a39299d175bc4")
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("\nTesting to receive a GET request error response with an invalid place_id was successful\n")

    @allure.description("Test update address operation failed, invalid place_id")
    def test_update_address_operation_failed(self):

        print("\nМетод PUT 404")
        result_put = Google_maps_api.put_new_place("f8e058584c3dc7ae3d74a39299d175bc4")
        Checking.check_status_code(result_put, 404)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', "Update address operation failed, looks like the data doesn't exists")

        print("\nTesting to receive a PUT request error response with an invalid place_id was successful\n")

    @allure.description("Test delete operation failed, invalid place_id")
    def test_delete_operation_failed(self):

        print("\nМетод DELETE 404")
        result_delete = Google_maps_api.delete_new_place("f8e058584c3dc7ae3d74a39299d175bc4")
        Checking.check_status_code(result_delete, 404)
        Checking.check_json_token(result_delete, ["msg"])
        Checking.check_json_value(result_delete, "msg", "Delete operation failed, looks like the data doesn't exists")

        print("\nTesting to receive a DELETE request error response with an invalid place_id was successful\n")








