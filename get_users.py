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
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if sys.platform == "win32":
    os.system("cls")
    oFile = f"{os.getcwd()}/output/users.json"
else:
    os.system("clear")
    oFile = f"{os.getcwd()}/output/users.json"

print(show_banner())
pprint("================= ")
pprint(" Get User Listing ")
pprint("================= ")

# Preparing global config
out_data = []
client_id = os.environ.get(Options.client_id)
client_secret = os.environ.get(Options.client_secret)
region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
PureCloudPlatformClientV2.configuration.verify_ssl = False
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Creates api client
api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
PureCloudPlatformClientV2.configuration.access_token = api.access_token

usr_api = PureCloudPlatformClientV2.UsersApi()
expand = ["languages,groups,team"]
sort_order = Options.sort_order
page_size = Options.page_size
page_number = Options.page_number

try:
    init_api = usr_api.get_users(page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand, state="any")
    max_page_count = init_api.page_count + 1
    for pg_nm in range(1, max_page_count):
        page_number = pg_nm
        resp = usr_api.get_users(page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand, state="any")
        time.sleep(0.3)
        if resp.total == 0:
            pprint("========= End Result =========")
            break
        else:
            result = json.loads(resp.to_json()).get("entities")
            out_data += result
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
    sys.exit(1)

f = open(oFile, "w", encoding="utf-8")
f.write(json.dumps(out_data))
f.close()
sys.exit(0)
