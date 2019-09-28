
import boto3
import os
session = boto3.Session(
    aws_access_key_id=os.environ['AWS_SERVER_PUBLIC_KEY'],
    aws_secret_access_key=os.environ['AWS_SERVER_SECRET_KEY'],
)
# Create an S3 client
# s3 = session.resource('s3')
s3 = session.client('s3')

filename = 'file.txt'
bucket_name = 'temp1-s3'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)