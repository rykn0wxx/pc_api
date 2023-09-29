# -*- coding: utf-8 -*-

# import sys
# import os
# import json
# import ssl
# import certifi
# import base64
# import requests
# import PureCloudPlatformClientV2
# from PureCloudPlatformClientV2.rest import ApiException
# from pprint import pprint
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from config.options import Options

for q in Options.purecloud_queues:
    print(len(q))
