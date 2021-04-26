import boto3

client = boto3.client("s3")

response = client.list_object(Bucket='my-first-cloud9-s3-demo')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket='my-first-cloud9-s3-demo',Key=content['Key'])
    print(content['key'],obj_dict['last_modified'])
