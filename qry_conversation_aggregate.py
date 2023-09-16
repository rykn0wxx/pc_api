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
    oFile = f"{os.getcwd()}\output\conversations_aggregate.json"
else:
    os.system("clear")
    oFile = f"{os.getcwd()}/output/conversations_aggregate.json"

print(show_banner())
pprint("=====================================")
pprint("- Querying Conversation Aggregates -")
pprint("=====================================")

# Preparing global config
output_data = []
client_id = os.environ.get(Options.client_id)
client_secret = os.environ.get(Options.client_secret)
region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
PureCloudPlatformClientV2.configuration.verify_ssl = False
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Creates api client
api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
PureCloudPlatformClientV2.configuration.access_token = api.access_token

# Main method to query the api
def query_conversations_aggregates():
    # Creates auth api instance
    out_data = []
    agg_api = PureCloudPlatformClientV2.AnalyticsApi(api)
    qry = PureCloudPlatformClientV2.ConversationAggregationQuery()
    queues_arr = Options.purecloud_queues
    qry.granularity = "PT30M"
    qry.flatten_multivalued_dimensions = True
    qry.group_by = ["conversationId","direction","queueId","requestedLanguageId","requestedRoutingSkillId","userId","dnis"]
    qry.metrics = ["nBlindTransferred","nConnected","nConsult","nConsultTransferred","nError","nOffered","nOutbound","nOverSla","nTransferred","tAbandon","tAcd","tAcw","tAlert","tAnswered","tContacting","tDialing","tFlowOut","tHandle","tHeldComplete","tIvr","tMonitoring","tNotResponding","tShortAbandon","tTalkComplete","tVoicemail","tWait"]
    try:
        #  Looping thru queues
        for q in queues_arr:
            qry.filter = {
                "type": "and",
                "clauses": [
                    {
                        "type": "or",
                        "predicates": q
                    },
                    {
                        "type": "or",
                        "predicates": [{ "dimension": "mediaType", "value": "voice" }]
                    }
                ]
            }
            # Looping thru months
            for mo in Options.reporting_week:
                qry.interval = mo
                resp = agg_api.post_analytics_conversations_aggregates_query(qry)
                results = json.loads(resp.to_json()).get("results")
                if type(results) != None.__class__:
                    out_data += results
                    pprint(f"=== interval: { mo } ===")
                    pprint(f"=== results: { len(results) } | output:{ len(out_data) } ===")
    except ApiException as e:
        pprint("Exception when calling post_analytics_conversations_aggregates_query: %s\n" % e)
        sys.exit(1)

    save_to_file(out_data)

def save_to_file(data):
    # oFile = r"/mnt/hgfs/mudhead/pc_api/output/conversations_aggregate.json"
    f = open(oFile, "w", encoding="utf-8")
    f.write(json.dumps(data))
    f.close()

if __name__ == "__main__":
    start_time = time.time()
    query_conversations_aggregates()
    pprint(f"---- StartTime: { start_time }")
    end_time = time.time()
    pprint(f"---- EndTime: { end_time }")
    print("--- %s seconds ---" % (end_time - start_time))
    sys.exit(0)
