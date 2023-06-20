import boto3
from botocore.exceptions import ClientError
from flask import Flask

app = Flask('RESTful')


client = boto3.client('dynamodb')


def create_table():
    table = client.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType':'HASH' #partition key
            },
            {
                'AttributeName': 'title',
                'KeyType':'RANGE' 
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName':'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName':'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits' : 20,
            'WriteCapacityUnits' : 20
        }
    )

    return table



def put_movie_item(title, year, **kwargs):
    response = client.put_item(
        TableName='Movies',
        Item={
            'year':{
                'N':'{}'.format(year),
            },
            'title':{
                'S':'{}'.format(title)
            },
            'rating': {
                'N':'{}'.format(kwargs['rating'])
            }
        }
    )

    return response


def update_movie(title, year, rating, director):
    response = client.update_item(
        TableName='Movies',
        Key={
            'year':{
                'N':'{}'.format(year)
            },
            'title':{
                'S':'{}'.format(title)
            }
        },
        ExpressionAttributeNames={
            '#R': 'rating',
            '#D': 'director'
        },
        ExpressionAttributeValues={
            ':r':{
                'N':'{}'.format(rating)
            },
            ':d':{
                'S':'{}'.format(director)
            }
        },
        UpdateExpression='SET #R = :r, #D = :d',
        ReturnValues='UPDATED_NEW'
    )

    return response

@app.get('/movies/<int:year>/<string:title>')
def get_movie(year, title):

    response = client.get_item(
        TableName='Movies',
        Key={
            'year': {
                'N':'{}'.format(year)
            },
            'title': {
                'S':'{}'.format(title)
            }
        }
    )
    return response


def delete_item(year, title, rating):
    resp = client.delete_item(
        TableName='Movies',
        Key={
            'year':{
                'N':'{}'.format(year)
            },
            'title':{
                'S':'{}'.format(title)
            }
        },
        ConditionExpression="rating <= :r",
        ExpressionAttributeValues={
            ':r': {
                'N':'{}'.format(rating)
            }
        }
    )

    return resp




# movie_table = create_table() 
# print(movie_table)

# put_res = put_movie_item('RRR', 2022, rating=4.5)
# print(put_res)

# resp = update_movie('RRR', 2022, 5, 'SSR')
# print(resp)

# resp = get_movie(2022, 'RRR')
# print(resp['Item'])


# resp = delete_item(2021, 'New Movie', 3)
# print(resp)

app.run()