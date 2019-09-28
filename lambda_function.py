import boto3
import json
import os


def lambda_handler(event, context):
    # TODO implement
    session = boto3.Session(
        aws_access_key_id=os.environ['AWS_SERVER_PUBLIC_KEY'],
        aws_secret_access_key=os.environ['AWS_SERVER_SECRET_KEY'],
    )
    # Create an S3 client
    s3 = session.resource('s3')
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_name = object_key.split('/').pop()
        s3_path = "/Processed/" + file_name
        uploadedfile = s3.Bucket(bucket_name).Object(object_key).get()
        content = uploadedfile['Body'].read()
        input_file = os.path.join(bucket_name,object_key)
        s3.Bucket(bucket_name).put_object(Key=s3_path, Body=content)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
