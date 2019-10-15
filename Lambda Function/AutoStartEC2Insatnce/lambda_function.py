import boto3
# Specify the region where your insatnces are running. For example 'ap-southeast-1'
region = 'ap-south-1'
# Specify the insatnce IDs that you want to start at specific time. For example, ['i-abcd01234567', 'i-efgh01234567']
instances = ['-------------']
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'started your instances: ' + str(instances)