
import requests

url = "http://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

print(response.json())


