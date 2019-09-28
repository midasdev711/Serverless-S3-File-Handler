# Serverless-S3-File-Handler
This separates out the processing of the file from the receipt of the file by using a Lambda function triggered by a file’s arrival.

# upload.py

You can upload file with this file.

## 1. Set environment variables 
  ### AWS_SERVER_PUBLIC_KEY = public key of your aws account
  ### AWS_SERVER_SECRET_KEY = secret key of your aws account
  ### FILE_NAME = file name you want to upload
  ### BUCKET_NAME = s3 bucket name
## 2. Run the script

# lambda_function.py

This is the lambda_function that is triggered when you upload file to s3.

## 1. Create Lambda function on your aws account.
  ### 1.1 Choose Author from scratch  
  ### 1.2 Input function name and choose python3.6 as language.  
  ### 1.3 Choose 'Upload a .zip file' in the Code entry type select box.
  ### 1.4 Upload the lambda_function.zip file.
  ### 1.5 Set Environment variables
    1.5.1 Set AWS_SERVER_PUBLIC_KEY as the public key of your aws account
    1.5.2 Set AWS_SERVER_SECRET_KEY as the secret key of your aws account
## 2. Create s3 bucket on your aws account.
  ### 2.1 You have to grant access to specific users.
    Check only 'Block public access to buckets and objects granted through new public bucket policies' and 'Block pulibic and cross-account access to buckets and objects through any public bucket policies' in the Block public acess settings.
  ### 2.2 In you s3 bucket, go to Properties, and add an event
    2.2.1 Choose PUT and POST for events.
    2.2.2 Choose Lambda function in the sendto select box.
    2.2.3 Choose Lambda function you defined in the Lambda select box.
  
