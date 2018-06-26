import json

# Our lambda handler function!
def lambda_handler(event, context):
    # Printing event received.
    print("Received event: " + json.dumps(event, indent=2))

    # Trying to print a variable that is not defined will result in a invocation error!
    # Comment it out in order to have your function succeed!
    print(not_defined)