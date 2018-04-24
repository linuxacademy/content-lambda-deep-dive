import json

print('Loading your function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # print statements actually get printed to the logs.
    print("message --> " + event['message'])

    # Actually returning the value of the 'message' key.
    return event['message']

    # Raising an exception if something goes wrong...
    raise Exception('Something went wrong!')
