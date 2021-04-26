import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('my-first-cloud9-s3-demo')

for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)
    
    
#   access client from resource
s3_client = boto3.resource('s3').meta.client
