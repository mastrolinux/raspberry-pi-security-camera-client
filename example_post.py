import requests

url = 'https://camera-server.onrender.com/upload'
file = {'media': open('/tmp/test.jpg', 'rb')}
resp = requests.post(url, files=files)

print (resp)
