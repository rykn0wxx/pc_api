# -*- coding: utf-8 -*-

import json
import os
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint
from config.options import Options

arr01 = [
    {
        "id": "1570f7ee-22f6-4e4a-ba60-9c0485eeca73",
        "name": "AasifThaliya Madakandi",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/1570f7ee-22f6-4e4a-ba60-9c0485eeca73"
    },
    {
        "id": "afb7aad1-2964-46b6-939f-bb6f338c5b38",
        "name": "AbdulMoiz Rawasia",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/afb7aad1-2964-46b6-939f-bb6f338c5b38"
    },
    {
        "id": "d5552e65-01c4-426d-8396-eac05b97150c",
        "name": "Aaron Badon",
        "acdAutoAnswer": "true",
        "selfUri": "/api/v2/users/d5552e65-01c4-426d-8396-eac05b97150c"
    },
    {
        "id": "eb4c0299-e23b-42fc-99b3-41acffdee98f",
        "name": "Abdulrahman Bakr",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/eb4c0299-e23b-42fc-99b3-41acffdee98f"
    },
    {
        "id": "fbda66e4-3039-4225-8b46-d3052cc34eb7",
        "name": "Abbey Christine Simeon",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/fbda66e4-3039-4225-8b46-d3052cc34eb7"
    }
]
arr02 = [
    {
        "id": "97498ae7-a987-4297-a64d-010da656fba3",
        "name": "Adrian Virlan",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/97498ae7-a987-4297-a64d-010da656fba3"
    },
    {
        "id": "0d71d3f7-6490-4647-a74f-3f4800c98f44",
        "name": "Adrian Tutulan",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/0d71d3f7-6490-4647-a74f-3f4800c98f44"
    },
    {
        "id": "62cc0148-24e5-4b8a-87f8-2556342df146",
        "name": "Adrian Marcel Sisestean",
        "acdAutoAnswer": "false",
        "selfUri": "/api/v2/users/62cc0148-24e5-4b8a-87f8-2556342df146"
    }
]

client_id = os.environ.get(Options.client_id)
client_secret = os.environ.get(Options.client_secret)
region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Creates api client
api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
PureCloudPlatformClientV2.configuration.access_token = api.access_token

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi();
page_size = 1 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = "ASC" # str | Ascending or descending sort order (optional) (default to 'ASC')
expand = ["languages,groups,team"] # list[str] | Which fields, if any, to expand (optional)
state = "any" # str | Only list users of this state (optional) (default to 'active')
out_data = []

try:
    # Get the list of available users.
    for pg_nm in range(1, 3):
        page_number = pg_nm
        api_response = api_instance.get_users(page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand, state=state)
        resp = json.loads(api_response.to_json()).get("entities")
        out_data += resp
        print(len(out_data))
    pprint(out_data)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
