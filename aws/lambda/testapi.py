import json

def lambda_handler(event, context):
    # TODO implement
    
    data = [
        {
            'student_name':'SCOTT',
            'student_id': 1001,
            'score': 98.5
        },
        {
            'student_name':'TIGER',
            'student_id': 1002,
            'score': 98.5
        },
        {
            'student_name':'JOHN',
            'student_id': 1003,
            'score': 98.5
        }
    ]
    
    print(event)
    
    if event['queryStringParameters']:
        result = {}
        for key,value in event['queryStringParameters'].items():
            print(key, value)
            for ele in data:
                print(ele, ele[key])
                if f'{ele[key]}' == f'{value}':
                # if ele[key] == value:
                    result = ele
                    break

        return {'statusCode': 200, 'body':json.dumps(result)}
        
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
