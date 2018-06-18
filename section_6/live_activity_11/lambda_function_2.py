import json
import os

print('---Loading function---')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    ip = event['requestContext']['identity']['sourceIp']

    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'Hello World!',
            'location': ip
        })
    }