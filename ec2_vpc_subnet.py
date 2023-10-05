import boto3
import json
from datetime import datetime

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# EC2 instance settings
instance_params = {
    'ImageId': 'ami-067d1e60475437da2',  # Image ID of the AMI
    'InstanceType': 't2.micro',  # Choose the desired instance type
    'KeyName': 'my-ec2-boto3-20231005152040',  # Replace with your key pair name
    'MinCount': 1,  # Minimum number of instances to launch
    'MaxCount': 1,  # Maximum number of instances to launch
    'NetworkInterfaces': [
        {
            'DeviceIndex': 0,
            'Groups': ['sg-085ebbc6e54bfa017'],  # Replace with your VPC security group ID
            'SubnetId': 'subnet-0f2081ea77cb9220c'  # Associate the instance with the private subnet
        }
    ],
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'INSTANCE_EC2_PRIVATE2',
                    'Value': f'MyEC2Private_{datetime.now().strftime("%Y%m%d%H%M%S")}'  # Add the current date and time to the name
                }
            ]
        }
    ]
}

# Create the EC2 instance associated with the security group and subnet
response = ec2_client.run_instances(**instance_params)

# Get the ID of the created instance
instance_id = response['Instances'][0]['InstanceId']

# Create a dictionary with instance details
instance_details = {
    'InstanceId': instance_id,
    'InstanceType': instance_params['InstanceType'],
    'SubnetId': instance_params['NetworkInterfaces'][0]['SubnetId'],  # Get the SubnetId from NetworkInterfaces
    'VpcSecurityGroupId': 'sg-085ebbc6e54bfa017',  # Replace with your VPC security group ID
    'CreationTime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Print instance details in JSON format
print(json.dumps(instance_details, indent=4))

