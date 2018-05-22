import json
import datetime
import time
import boto3


## Importing ec2 boto3 client.
ec2 = boto3.client('ec2')

## Importing SNS client.
sns = boto3.client('sns')

print('     !Running your function!     ')


def lambda_handler(event, context):
    #print(event)

    ## Getting the Instance ID of the instance that is shutting down.
    instanceID = event['detail']['instance-id']

    instances = ec2.describe_instances(
        InstanceIds=[
            instanceID,
        ]
    )

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for device in instance['BlockDeviceMappings']:
                ebs = device['Ebs']['VolumeId']
                print("We are taking a snapshot of volume -- %s" % ebs)

                ec2.create_snapshot(
                    Description='From instance: %s' % instanceID,
                    VolumeId=ebs,
                )

                # Sending admin email.
                sns.publish(
                    ## EDIT THE ARN
                    TopicArn='ARN',
                    Message='Your rule has been triggered to create a snapshot for the following volume -- Volume ID: ' + ebs,
                    Subject='Snapshot Occurred'
                )

