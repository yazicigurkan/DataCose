import requests
import json
import datetime


class UserContactConverter(object):
    def __init__(self, url: str, method_get_token: str, method_post_token: str):

        self.url = url
        self.method_get_token = method_get_token
        self.method_post_token = method_post_token

    def prepare_payload(self, pre_payload: dict):

        pre_fields = pre_payload["fields"]

        first_name, last_name = self.data_cleaner(
            pre_fields["firstName"],
            pre_fields["lastName"],
        )
        birthdate, lifetime = self.transfor_data(
            pre_fields["dateOfBirth"],
            pre_fields["lifetime_value"],
        )

        payload_schema = {
            "birthdate": pre_fields["dateOfBirth"],
            "email": pre_fields["email"],
            "custom_properties": {
                "airtable_id": pre_payload["id"],
                "lifetime_value": pre_fields["lifetime_value"],
            },
        }
        payload_schema["first_name"] = first_name
        payload_schema["last_name"] = last_name
        payload_schema["birthdate"] = birthdate
        payload_schema["custom_properties"]["lifetime_value"] = lifetime

        return payload_schema

    def transfor_data(self, birth_date: str, lifetime: str):
        birth_date = datetime.datetime.strptime(birth_date, "%d-%m-%Y").strftime(
            "%Y-%m-%d"
        )
        lifetime = float(lifetime[1:])

        return birth_date, lifetime

    def data_cleaner(self, first_name: str, last_name: str):

        return first_name.strip(), last_name.strip()

    def get_users(self):
        path = "/people/"
        url = "{}{}".format(self.url, path)

        headers = {"Authorization": "Bearer {}".format(self.method_get_token)}

        response = requests.request("GET", url, headers=headers)

        for user in json.loads(response.text):
            yield user

    def create_contact(self, payload: dict):

        path = "/contacts/"
        url = "{}{}".format(self.url, path)

        payload = json.dumps(payload)
        headers = {"Authorization": "Basic {}".format(self.method_post_token)}

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.status_code
