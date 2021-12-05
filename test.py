import requests
import json

url = 'http://127.0.0.1:8000/api/viewInstaProfile/gdscgndu'
# url = 'https://bucketapigdscgndu.herokuapp.com/api/viewInstaProfile/?username=__sairish__'
data = {'username': "gdscgndu"}
data = json.dumps(data)
r = requests.post(url, data = data)
print(r.text)

