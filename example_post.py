import requests

url = 'https://camera-server.onrender.com/upload'
files = {'file': open('/tmp/2022-04-10T20:57:06.706411.jpg', 'rb')}
r = requests.post(url, files=files)

print (r.json())
r.raise_for_status()
