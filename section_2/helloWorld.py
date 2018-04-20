import json

print('Loading your function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("message --> " + event['message'])

    return event['message']  # Echo back the first key value
    raise Exception('Something went wrong!')
