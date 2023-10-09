# Initialize the Client Boto3
ec2_client = boto3.client('ec2')

# ID VPC where you desired create your NAT Gateway
vpc_id = 'vpc-0753d54754dd2c70a'

# Create a new IP Elastic (EIP)
eip_response = ec2_client.allocate_address()

# Getting a Allocation ID EIP
allocation_id = eip_response['AllocationId']

# Creating the NAT Gateway 
nat_gateway_response = ec2_client.create_nat_gateway(
    SubnetId='subnet-0f2081ea77cb9220c',
    AllocationId=allocation_id
)

# Getting the ID NAT Gateway 
nat_gateway_id = nat_gateway_response['NatGateway']['NatGatewayId']

# Creating an Dic with a function to show the details of NAT Gateway 
nat_gateway_details = {
    'NatGatewayId': nat_gateway_id,
    'VpcId': vpc_id,
    'SubnetId': 'sua_subnet_id_aqui',
    'AllocationId': allocation_id,
    'CreationTime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Print the details 
print(json.dumps(nat_gateway_details, indent=4))
