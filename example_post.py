import requests

url = 'https://camera-server.onrender.com/upload'
files = {'media': open('/tmp/test.jpg', 'rb')}
r = requests.post(url, files=files)

print (r.status_code)
