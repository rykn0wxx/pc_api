# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import sys
import json
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint
from banner import show_banner
from config.options import Options

os.system("clear")
print(show_banner())

pprint(f" Get User Login Logout ")

# Preparing global config
out_data = []
client_id = os.environ.get(Options.client_id)
client_secret = os.environ.get(Options.client_secret)
region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Creates api client
api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
PureCloudPlatformClientV2.configuration.access_token = api.access_token

usr_api = PureCloudPlatformClientV2.UsersApi()
usr_filter = PureCloudPlatformClientV2.UserDetailsQuery()
usr_filter.interval = "2023-07-01T08:00:00.000Z/2023-08-01T08:00:00.000Z"
usr_filter.user_filters = [
    {
        "type": "or",
        "predicates": [
            { "type": "dimension", "dimension": "userId", "value": "141ef72c-c244-4b32-be80-a5d21f3d2d80" },
            { "type": "dimension", "dimension": "userId", "value": "5348d081-8be9-4c76-85c0-46dcf0f66484" },
            { "type": "dimension", "dimension": "userId", "value": "b31b9409-29c9-4124-9376-fb8d0658cdab" },
            { "type": "dimension", "dimension": "userId", "value": "8579140d-3f68-4c45-a032-3e67eafd1fa2" },
            { "type": "dimension", "dimension": "userId", "value": "0c9aff9a-b6db-4f34-809e-c025176f41d3" },
            { "type": "dimension", "dimension": "userId", "value": "bb6a3bdf-5f4a-4544-b8c9-6f3eb3584cfe" },
            { "type": "dimension", "dimension": "userId", "value": "014e3a40-e794-477d-8c2d-1c633ef0139e" },
            { "type": "dimension", "dimension": "userId", "value": "4dfec75d-6efd-46e4-bbf2-c61f93e46146" },
            { "type": "dimension", "dimension": "userId", "value": "271edcfd-bca3-4e56-92cc-3e2d052d7482" },
            { "type": "dimension", "dimension": "userId", "value": "685b45cb-7dee-4a12-b317-d68c9c58ae37" },
            { "type": "dimension", "dimension": "userId", "value": "400ffbcb-2954-4961-90c8-f5d7383ff461" },
            { "type": "dimension", "dimension": "userId", "value": "1d92bd11-b5df-427a-be8e-9d03eb45f98f" },
            { "type": "dimension", "dimension": "userId", "value": "85f4f9c6-5466-447a-8651-c211ef212e4f" },
            { "type": "dimension", "dimension": "userId", "value": "7fe7433d-dc86-4d66-a339-39a7a237d8d0" },
            { "type": "dimension", "dimension": "userId", "value": "af5a00d3-5700-4b53-853c-78ba4f6009e1" },
            { "type": "dimension", "dimension": "userId", "value": "89c18803-d63a-456a-80b7-452d734295f2" },
            { "type": "dimension", "dimension": "userId", "value": "bc415ead-7a8c-4339-a74e-0370b7b65adf" },
            { "type": "dimension", "dimension": "userId", "value": "9ea740b4-d0e0-49ea-adec-1c3e6636ccc6" },
            { "type": "dimension", "dimension": "userId", "value": "d1872b79-6d11-4398-a779-eda9e8931fbc" },
            { "type": "dimension", "dimension": "userId", "value": "5834c38b-b65b-4b82-8609-1dce6ff39bd1" },
            { "type": "dimension", "dimension": "userId", "value": "18fc9fba-ab14-4200-8250-e39557577c91" },
            { "type": "dimension", "dimension": "userId", "value": "8bd881ef-2753-4f7c-aa95-0f4a9cc3fe5d" },
            { "type": "dimension", "dimension": "userId", "value": "bd8ff873-d750-4e19-a643-47e22b3c46ce" },
            { "type": "dimension", "dimension": "userId", "value": "3ff8afcb-3a98-446f-9b9c-961047ae6316" },
            { "type": "dimension", "dimension": "userId", "value": "9a2b5cb9-ca5a-4194-a40f-c401f7dec857" },
            { "type": "dimension", "dimension": "userId", "value": "81ac65da-8aa9-4af6-965a-1d882465f0ce" },
            { "type": "dimension", "dimension": "userId", "value": "a6f7552c-532b-4d65-a912-1926cf68e1ca" },
            { "type": "dimension", "dimension": "userId", "value": "51d7a0b2-daf7-4134-9b9b-ee7856faa274" },
            { "type": "dimension", "dimension": "userId", "value": "b63cc4fa-ea7a-40e1-8dd9-45df15ada420" },
            { "type": "dimension", "dimension": "userId", "value": "f90cce21-94ef-4a9d-88b3-607a86070880" },
            { "type": "dimension", "dimension": "userId", "value": "62e9dc03-9927-49e7-bafd-057b43838cb0" },
            { "type": "dimension", "dimension": "userId", "value": "1883e221-1afd-4615-aed0-19bca5d284eb" },
            { "type": "dimension", "dimension": "userId", "value": "9836dc4e-0653-4d9f-90eb-9fd5cad0a03f" },
            { "type": "dimension", "dimension": "userId", "value": "a7cae2c8-3042-4dae-b5a7-8c97b6620c1a" },
            { "type": "dimension", "dimension": "userId", "value": "96bd415a-8e33-404c-a221-3dc817beb010" },
            { "type": "dimension", "dimension": "userId", "value": "5f5279f8-acef-4111-ab0c-ccc12022df2f" },
            { "type": "dimension", "dimension": "userId", "value": "6e1bbdf6-34b0-4dd2-aa2c-47faacc855cd" },
            { "type": "dimension", "dimension": "userId", "value": "39e7cfbd-66d1-4d70-966b-33346de707b1" },
            { "type": "dimension", "dimension": "userId", "value": "cb8f1fd8-6aa2-46ca-87b9-a7456a0ee9a4" },
            { "type": "dimension", "dimension": "userId", "value": "b4fdea90-9a4c-4867-ad1f-4171814c33b2" },
            { "type": "dimension", "dimension": "userId", "value": "8d8231bf-1448-42b7-96df-f10e4f02640e" },
            { "type": "dimension", "dimension": "userId", "value": "52d74123-c951-424a-8c80-abc3d115178d" },
            { "type": "dimension", "dimension": "userId", "value": "cf301cb7-abea-4b82-a61f-9705c09f1a4e" },
            { "type": "dimension", "dimension": "userId", "value": "2731620b-79e4-4402-82ef-76546705e132" },
            { "type": "dimension", "dimension": "userId", "value": "d5e8738e-4de0-4db9-9281-db2ec9cda377" },
            { "type": "dimension", "dimension": "userId", "value": "cf51534f-4127-4970-8c1b-067c70989cc9" }
        ]
    }
]
usr_filter.presence_filters = [
    {
        "type": "and",
        "predicates": [
            {
                "type": "dimension",
                "dimension": "systemPresence",
                "value": "OFFLINE"
            }
        ]
    }
]
usr_filter.order = Options.sort_order
usr_filter.paging = {
    "pageSize": 100,
    "pageNumber": 1
}

try:
    init_api = usr_api.post_analytics_users_details_query(usr_filter)
    max_rec = round(init_api.total_hits / 100) + 1
    for pg_nm in range(1, max_rec):
        usr_filter.paging = {
            "pageSize": 100,
            "pageNumber": pg_nm
        }
        resp = usr_api.post_analytics_users_details_query(usr_filter)
        time.sleep(0.3)
        results = json.loads(resp.to_json()).get("user_details")
        if type(results) != None.__class__:
            out_data += results
            pprint(f"=== results: { len(results) } | { pg_nm } of { max_rec } ===")
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_details_query: %s\n" % e)
    sys.exit(1)

oFile = f"{os.getcwd()}/output/user_lilo.json"
f = open(oFile, "w", encoding="utf-8")
f.write(json.dumps(out_data))
f.close()
