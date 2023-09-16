# -*- coding: utf-8 -*-

import sys
import os
import json
import ssl
import certifi
import base64
import requests
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ssl.CERT_NONE
# ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
# ssl._create_default_https_context = ssl._create_unverified_context
client_id = os.environ.get("PURECLOUD_CLIENTID")
client_secret = os.environ.get("PURECLOUD_SECRET")
# PureCloudPlatformClientV2.configuration.verify_ssl = False
# # # print(certifi.where())
# region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
# PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# # # Creates api client
# api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
# PureCloudPlatformClientV2.configuration.access_token = api.access_token

# # # Creates auth api instance
# agg_api = PureCloudPlatformClientV2.AnalyticsApi(api)
# qry = PureCloudPlatformClientV2.ConversationAggregationQuery()

# # # Build the body query
# qry.interval = "2023-09-04T00:00:00.000Z/2023-09-11T00:00:00.000Z"
# qry.granularity = "P1D"
# qry.flatten_multivalued_dimensions = True
# qry.time_zone = "Etc/UTC"
# qry.group_by = ["direction", "queueId"]
# qry.metrics = ["nOffered", "tAcd", "tHandle"]
# qry.filter = {
#     "type": "and",
#     "clauses": [
#         {
#             "type": "or",
#             "predicates": [
#                 {
#                     "type": "dimension",
#                     "dimension": "queueId",
#                     "operator": "matches",
#                     "value": "07ff1769-a0a6-4cac-bbe4-700329d29cfc"
#                 },
#                 {
#                     "type": "dimension",
#                     "dimension": "queueId",
#                     "operator": "matches",
#                     "value": "f42496f0-0b71-4d9b-8a4d-d96dd4c6242b"
#                 }
#             ]
#         },
#         {
#             "type": "or",
#             "predicates": [
#                 {
#                     "type": "dimension",
#                     "dimension": "mediaType",
#                     "operator": "matches",
#                     "value": "voice"
#                 }
#             ]
#         }
#     ]
# }

# def main_function():
#     try:
#         oFile = f"{os.getcwd()}\output\sandbox_results.json"
#         resp = agg_api.post_analytics_conversations_aggregates_query(qry)
#         results = json.loads(resp.to_json()).get("results")
#         f = open(oFile, "w", encoding="utf-8")
#         f.write(json.dumps(results))
#         f.close()
#     except ApiException as e:
#         pprint("Exception when calling post_analytics_conversations_aggregates_query: %s\n" % e)
#         sys.exit(1)

# if __name__ == "__main__":
#     main_function()
#     sys.exit(0)


# authorization = base64.b64encode(bytes(client_id + ":" + client_secret, "ISO-8859-1")).decode("ascii")
# request_headers = {
#     "Authorization": f"Basic {authorization}",
#     "Content-Type": "application/x-www-form-urlencoded"
# }
# request_body = {
#     "grant_type": "client_credentials"
# }
# resp = requests.post("https://login.mypurecloud.de/oauth/token", data=request_body, headers=request_headers, verify=False)

# print(resp)

# auth_str = 'Basic ' + base64.b64encode(bytes((client_id + ':' + client_secret).encode('ascii'))).decode(
#     'ascii')

# auth_str = 'Basic ' + base64.b64encode(bytes((client_id + ':' + client_secret).encode('ascii'))).decode(
#     'ascii')
cis = " ".join([client_id, ':', client_secret]).encode('ascii')
print(cis)

