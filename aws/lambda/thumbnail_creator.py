
import json
from thumbnail import generate_thumbnail

def create_thumbnail(event, context):
    options = {
        'trim': False,
        'height': 300,
        'width': 300,
        'quality': 85,
        'type': 'thumbnail'
    }

    bucket = event['s3']['bucket']['name']
    object = event['s3']['bucket']['object']['key']
    source = f's3://{bucket}/{object}'
    target = f's3://{bucket}/thumb/{object.split('/')[-1]}'
    print(source, target)

    generate_thumbnil(source, target, options)

    