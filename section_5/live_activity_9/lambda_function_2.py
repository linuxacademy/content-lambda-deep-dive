import json
import boto3

# Setting ec2 client.
ec2 = boto3.client('ec2')

# Our lambda handler function!
def handler(event, context):
    # Printing event received.
    # print("Received event: " + json.dumps(event, indent=2))

    # Let's go ahead and print the rule arn to the logs so we know they are different!
    rule_name = event['resources']
    print(rule_name)

    # Setting the variable to loop through later.
    # Filtering by only looking for 'in-use' EBS volumes.
    total_ebs = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['in-use']}])

    # Looping through and collecting all EBS volumes.
    for volume in total_ebs['Volumes']:
    	# Setting description for later use.
        # description = volume['Attachments'][0]['InstanceId']

    	# Creating the snaphsot for all volumes within our region.
        # ec2.create_snapshot(VolumeId=volume['VolumeId'],Description=volume['Attachments'][0]['InstanceId'])
        ec2.create_snapshot(VolumeId=volume['VolumeId'],Description='Created by the live activity students!')

        print("All done with volume: " + volume['VolumeId'])