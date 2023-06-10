data = {
    'userId': 4, 
    'title': 'xyz', 
    'completed': True,
    'id':1
    }

import requests

url = "http://jsonplaceholder.typicode.com/todos"
response = requests.post(url, json=data)

print('status', response.status_code)
print('output', response.json())