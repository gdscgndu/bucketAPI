import requests
import json

url = 'http://127.0.0.1:8000/api/viewInstaProfile/'
data = {'username': "gdscgndu"}
data = json.dumps(data)
r = requests.get(url, data = data)
print(r.text)
