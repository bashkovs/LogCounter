import requests

img_path = "test_image.jpeg"
headers = {"Content-type": "image/jpg"}
url = "http://0.0.0.0:5005/recognize"

files = open(img_path, "rb").read()
r = requests.post(url, data=files, headers=headers)
print("Status code:", r.status_code)

if r.status_code == 200:
    print(r.json())
