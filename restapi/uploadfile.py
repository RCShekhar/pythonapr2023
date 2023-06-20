import boto3

s3 = boto3.client('s3')

#/Users/rachakonda/PythonTraining/restapi/response.json

def upload_file(file_path):
    response = s3.upload_file(
        Filename=file_path,
        Bucket='test-bkt-training',
        Key='myresponse.json'
    )
    return response

def download_file(bucket, file_name, local_file):
    s3.download_file(
        Bucket=bucket,
        Key=file_name,
        Filename=local_file
    )


def create_bucket(bkt_name):
    resp = s3.create_bucket(Bucket=bkt_name,
                     CreateBucketConfiguration={
                         'LocationConstraint': 'us-east-2'
                     })
    return resp


def list_buckets():
    buckts = []
    resp = s3.list_buckets()

    l = resp['Buckets']
    buckts = [d['Name'] for d in l]

    return buckts


def delete_bucket(bkt_name):
    res = s3.delete_bucket(Bucket=bkt_name)

    return res
# res = upload_file('/Users/rachakonda/PythonTraining/restapi/response.json')
# print(res)

# download_file('test-bkt-training', 'myresponse.json', '/Users/rachakonda/PythonTraining/restapi/mrp.json')

# resp = create_bucket('aws-learning-20062023-1')
# print(resp)

# print(list_buckets())

res = delete_bucket('aws-learning-20062023')
print(res)
