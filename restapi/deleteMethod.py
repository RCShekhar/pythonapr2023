
import requests

url = "http://jsonplaceholder.typicode.com/todos/1"

response = requests.delete(url)

print(response.status_code)
print(response.json())


