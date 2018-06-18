import json

print('---Loading function---')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'Your code is working!'
        })
    }