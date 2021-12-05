import requests
import json

url = 'http://127.0.0.1:8000/api/viewInstaProfile/gdscgndu'
# url = 'https://bucketapigdscgndu.herokuapp.com/api/0/viewInstaProfile/__sairish__'
# data = {'username': "gdscgndu"}
# data = json.dumps(data)
# r = requests.post(url, data = data)
r= requests.post(url)
print(r.text)


# import instaloader
 
# ig = instaloader.Instaloader()
# # dp = input("Enter Insta username : ")
# dp="__sairish__"
 
# ig.download_profile(dp , profile_pic_only=True)
