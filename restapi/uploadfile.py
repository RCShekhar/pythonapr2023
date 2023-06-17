import boto3

s3_client = boto3.client('s3')

response = s3_client.upload_file(
    '/Users/rachakonda/PythonTraining/db.sqlite', 
    "test-bkt-training", 
    "db.sqlite" )