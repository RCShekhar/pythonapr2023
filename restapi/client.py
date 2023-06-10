import requests
import time

def getnewurl():
    std_url = "https://generate-new-url.com"    
    response = requests.get(std_url) # {'url':'http://webapi-timed-url.com', 'limit':'45mins'}
    return dict(response.json())['url']


api_url = getnewurl()
starttime = time.time()
while True:
    

    data = requests.get(api_url)

    endtime = time.time()
    if endtime - starttime >= 45:
        api_url = getnewurl()
        starttime = time.time()
    print(data)


