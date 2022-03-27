import logging as logger
import shutil
from pprint import pprint
from urllib.parse import urljoin

import requests
from assertpy import assert_that


class TestDogsAPI(object):

    def test_list_all_breeds(self, base_uri):
        """API request to produce a list of all dog breeds"""
        response = requests.get(urljoin(base_uri, "api/breeds/list/all"))
        assert_that(response.status_code).is_equal_to(200)
        pprint(response.json()["message"])

    def test_verify_item_in_list(self, base_uri):
        """Verify “retriever” breed is within the list."""
        breed = "retriever"
        response = requests.get(urljoin(base_uri, "api/breeds/list/all"))
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()["message"], f"Response does not contain {breed}").contains(breed)
        logger.info("\nVerify - retriever is within list")

    def test_verify_sub_breeds_in_list(self, base_uri):
        """API request to produce a list of sub-breeds for 'retriever'"""
        breed = "retriever"
        response = requests.get(urljoin(base_uri, "api/breeds/list/all"))
        assert_that(response.status_code).is_equal_to(200)
        sub_breeds = response.json()["message"][breed]
        logger.info(sub_breeds)

    def test_api_produce_random_image(self, base_uri):
        """API request to produce a random image / link for the sub-breed 'golden"""
        response = requests.get(urljoin(base_uri, "api/breeds/image/random"))
        assert_that(response.status_code).is_equal_to(200)
        image_url = response.json()["message"]
        rand_image = requests.get(image_url, stream=True)
        logger.info(f"\nRandom image link is: {image_url}")
        logger.info(f"\nRandom image saved in: /images/image.jpg")
        with open('./images/image.jpg', 'wb') as out_file:
            shutil.copyfileobj(rand_image.raw, out_file)
        del response
