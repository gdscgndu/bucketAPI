import requests
import json

url = 'http://127.0.0.1:8000/api/countchar/'
data = {'text': "Hello world"}
data = json.dumps(data)
r = requests.get(url, data = data)
print(r.text)