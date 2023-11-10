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
    oFile = f"{os.getcwd()}\output\pc_queues.json"
else:
    os.system("clear")
    oFile = f"{os.getcwd()}/output/pc_queues.json"

print(show_banner())
print(" Get Queue Listing ")

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

sort_order = Options.sort_order
page_size = Options.page_size
page_number = Options.page_number
api_inst = PureCloudPlatformClientV2.RoutingApi(api)

# Main method to query the api
def get_queue_list():
    out_data = []
    try:
        init_api = api_inst.get_routing_queues(page_number=page_number, page_size=page_size, sort_order=sort_order)
        max_page_count = init_api.page_count + 1
        for pg_nm in range(1, max_page_count):
            resp = api_inst.get_routing_queues(page_number=pg_nm, page_size=page_size, sort_order=sort_order)
            time.sleep(0.3)
            results = json.loads(resp.to_json()).get("entities")
            if type(results) != None.__class__:
                out_data += results
                pprint(f"=== { pg_nm } of { max_page_count } ===")
    except ApiException as e:
        print("Exception when calling RoutingApi->get_routing_queues: %s\n" % e)
        sys.exit(1)

    save_to_file(out_data)

def save_to_file(data):
    f = open(oFile, "w", encoding="utf-8")
    f.write(json.dumps(data))
    f.close()

if __name__ == "__main__":
    start_time = time.time()
    get_queue_list()
    pprint(f"---- StartTime: { start_time }")
    end_time = time.time()
    pprint(f"---- EndTime: { end_time }")
    print("--- %s seconds ---" % (end_time - start_time))
    sys.exit(0)
