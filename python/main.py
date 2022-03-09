import boto3


# create the object
def create_cloud9(subnet_id):
    response = client.create_environment_ec2(
        name='Cloud9-Test',
        description='A Cloud9 environment.',
        # clientRequestToken='string',
        instanceType='t2.micro',
        # hard-code this for the moment
        subnetId=subnet_id,
        imageId='amazonlinux-2-x86_64',
        automaticStopTimeMinutes=30,
        # ownerArn='string',
        tags=[
            {
                'Key': 'name',
                'Value': 'My-Test-Cloud9'
            },
        ],
        # connectionType='CONNECT_SSM'#,
        dryRun=True,
    )

    return response


if __name__ == '__main__':

    # get a reference to a Cloud9 object
    client = boto3.client('cloud9')

    # create a resource service client using the default region
    ec2 = boto3.resource('ec2', region_name=client.meta.region_name)
    
    # check for default vpc
    default_vpc_exists = False

    # present information to user
    for vpc in ec2.vpcs.all():
        the_vpc = ec2.Vpc(vpc.id)

        if the_vpc.is_default:
            default_vpc_exists = True
            print(f"The default region is: {client.meta.region_name}")
            print(f"The default VPC is: {vpc.id}")
            # use the first subnet
            the_subnet = list(the_vpc.subnets.all())[0]
            print(f"The availability zone is: {the_subnet.availability_zone}")
            print(f"Cloud9 will be deployed to subnet: {the_subnet.id}")
            response = create_cloud9(the_subnet.id)
            print(response)

    if not default_vpc_exists:
        print(f"A default VPC with public subnets is required to proceed.")




