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
pprint(" Get Queue Listing ")

# Preparing global config
out_data = []
client_id = os.environ.get(Options.client_id)
client_secret = os.environ.get(Options.client_secret)
region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Creates api client
api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
PureCloudPlatformClientV2.configuration.access_token = api.access_token

q_arrs = Options.purecloud_queues

for q_arr in q_arrs:
    for q in q_arr:
        print(q)
