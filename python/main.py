import boto3


# create the object
def create_cloud9():
    response = client.create_environment_ec2(
        name='Cloud9-Test',
        description='A Cloud9 environment.',
        # clientRequestToken='string',
        instanceType='t2.micro',
        # hard-code this for the moment
        subnetId='subnet-0d2f96fa7c8f48a1d',
        imageId='amazonlinux-2-x86_64',
        automaticStopTimeMinutes=30,
        # ownerArn='string',
        tags=[
            {
                'Key': 'name',
                'Value': 'My-Test-C9'
            },
        ],
        # connectionType='CONNECT_SSM'#,
        # dryRun=True,
    )

    return response


if __name__ == '__main__':

    # get a reference to a Cloud9 object
    client = boto3.client('cloud9')

    # create a resource service client using the default region
    ec2 = boto3.resource('ec2', region_name=client.meta.region_name)
    
    for vpc in ec2.vpcs.all():
        print(vpc.id)
        print(f"Is default? {ec2.Vpc(vpc.id).is_default}")




