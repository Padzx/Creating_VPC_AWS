import boto3
import json
from datetime import datetime

class VPCManager:
    def __init__(self):
        # Initialize your VPC client
        self.vpc_client = boto3.client('ec2')

    def create_vpc(self, cidr_block, vpc_name=None):
        # Get the current time 
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create the VPC
        response = self.vpc_client.create_vpc(
            CidrBlock=cidr_block,
            AmazonProvidedIpv6CidrBlock=False
        )
        
        # Get the VPC ID from the response
        vpc_id = response['Vpc']['VpcId']

        # Add a name tag to the VPC
        if vpc_name:
            vpc_name_with_timestamp = f"{vpc_name} ({current_time})"
            self.vpc_client.create_tags(
                Resources=[vpc_id],
                Tags=[
                    {
                        'Key': 'Name',
                        'Value': vpc_name_with_timestamp
                    }
                ]
            )

        # Return the answer in JSON format
        return json.dumps(response, indent=4)

if __name__ == "__main__":
    # Initialize the VPCManager class
    vpc_manager = VPCManager()

    # Define the CIDR block and the name of the VPC
    cidr_block = '10.0.0.0/16'
    vpc_name = 'VPC_NAME_BOTO3'

    # Create the VPC and print the response
    vpc_json_response = vpc_manager.create_vpc(cidr_block, vpc_name)
    print(vpc_json_response)
