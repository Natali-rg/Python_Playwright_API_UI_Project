
import os

import requests
from assertpy import assert_that
from dotenv import load_dotenv


load_dotenv()


class GorestUser:
    BASE_URL = os.getenv("BASE_URL")
    PATH = "public/v2/users"
    TOKEN = os.getenv("TOKEN")

    def user_get(self, param=None, user_id=None, exp_status_code=200):
        url = f"{self.BASE_URL}/{self.PATH}"

        if user_id:
            url += f"/{user_id}"

        response = requests.get(
            url=url,
            params=param,
            headers={"Authorization": f"Bearer {self.TOKEN}"}
            )
            
        

        assert_that(
            response.status_code,
            f"Wrong status code: {response.status_code}"
        ).is_equal_to(exp_status_code)

        return response.json()

    def user_post(self, dict_validate, exp_status_code=201):
        response = requests.post(
            url=f"{self.BASE_URL}/{self.PATH}",
            headers={
                "Authorization": f"Bearer {self.TOKEN}"
            },
            data=dict_validate
        )

        assert_that(
            response.status_code,
            f"Wrong status code: {response.status_code}"
        ).is_equal_to(exp_status_code)

        return response.json()

    def user_patch(self, user_id, dict_validate, exp_status_code=200):
        response = requests.patch(
            url=f"{self.BASE_URL}/{self.PATH}/{user_id}",
            headers={
                "Authorization": f"Bearer {self.TOKEN}"
            },
            data=dict_validate
        )

        assert_that(
            response.status_code,
            f"Wrong status code: {response.status_code}"
        ).is_equal_to(exp_status_code)

        return response.json()

    def user_put(self, user_id, dict_validate, exp_status_code=200):
        response = requests.put(
            url=f"{self.BASE_URL}/{self.PATH}/{user_id}",
            headers={
                "Authorization": f"Bearer {self.TOKEN}"
            },
            data=dict_validate
        )

        assert_that(
            response.status_code,
            f"Wrong status code: {response.status_code}"
        ).is_equal_to(exp_status_code)

        return response.json()

    def user_delete(self, user_id, exp_status_code=204):
        response = requests.delete(
            url=f"{self.BASE_URL}/{self.PATH}/{user_id}",
            headers={
                "Authorization": f"Bearer {self.TOKEN}"
            }
        )

        assert_that(
            response.status_code,
            f"Wrong status code: {response.status_code}"
        ).is_equal_to(exp_status_code)

        return response.status_code






