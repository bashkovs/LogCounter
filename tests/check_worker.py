import requests

img_path = "test_image_1.jpeg"
url = "http://0.0.0.0:5005/recognize/"

files = {"image": open(img_path, "rb")}
r = requests.post(url, files=files)

print("Status code:", r.status_code)

if r.status_code == 200:
    print(r.json())
