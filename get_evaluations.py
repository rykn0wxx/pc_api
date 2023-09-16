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
pprint("==============================")
pprint("- Querying Evaluations Data -")
pprint("==============================")

# Preparing global config
client_id = os.environ.get(Options.client_id)
client_secret = os.environ.get(Options.client_secret)
region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Creates api client
api = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
PureCloudPlatformClientV2.configuration.access_token = api.access_token
qa_api = PureCloudPlatformClientV2.QualityApi(api)

def get_qa_evaluations():
    qa_data = []
    qry = PureCloudPlatformClientV2.EvaluationAggregationQuery()
    qry.interval = "2023-08-07T00:00:00.000Z/2023-08-28T00:00:00.000Z"
    qry.granularity = "P1D"
    qry.time_zone = "Etc/UTC"
    qry.group_by = [
        "userId",
        "conversationId",
        "evaluationId"
    ]
    qry.metrics = [
        "nEvaluations"
    ]
    qry.flatten_multivalued_dimensions = True
    qry.alternate_time_dimension = "evaluationReleaseDate"

    try:
        eval_resp = qa_api.post_analytics_evaluations_aggregates_query(qry)
        evals = json.loads(eval_resp.to_json()).get("results")
        for eval in evals:
            qa_data.append({
                "conversationId": eval["group"]["conversationId"],
                "evaluationId": eval["group"]["evaluationId"]
            })
    except ApiException as e:
        print("Exception when calling QualityApi->post_analytics_evaluations_aggregates_query: %s\n" % e)
        sys.exit(1)
    return qa_data

def get_evaluation_aggregate(qa_evals):
    evals_agg = []
    expand = "evaluationForm"
    try:
        for qa_eval in qa_evals:
            agg_resp = qa_api.get_quality_conversation_evaluation(qa_eval["conversationId"], qa_eval["evaluationId"], expand=expand)
            evals_agg.append(json.loads(agg_resp.to_json()))
            time.sleep(0.3)
    except ApiException as e:
        print("Exception when calling QualityApi->get_quality_conversation_evaluation: %s\n" % e)
        sys.exit(1)
    return evals_agg

def save_data_to_file(data):
    mFile = f"{os.getcwd()}/output/qa_evals.json"
    main_file = open(mFile, "r", encoding="utf-8")
    main_data = json.load(main_file)
    main_file.close()
    out_data = main_data + data
    print(f"== main_file: { len(main_data) } | new_data: { len(data) } ==")
    oFile = open(mFile, "w", encoding="utf-8")
    oFile.write(json.dumps(out_data))
    oFile.close()

if __name__ == "__main__":
    try:
        print("Getting Evaluations")
        qa_eval_data = get_qa_evaluations()

        print(f"Getting QA Evaluation Aggregate for { len(qa_eval_data) }.")
        qa_data = get_evaluation_aggregate(qa_eval_data)

        print("Saving extrated data...")
        save_data_to_file(qa_data)
        sys.exit(0)
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.2)
        sys.exit(1)
