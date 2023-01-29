from requests import Response

from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""

class Test_create_place():

    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("\nМетод GET")
        result_get = Google_maps_api.get_new_place(place_id)