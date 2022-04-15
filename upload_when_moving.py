from gpiozero import MotionSensor
from picamera2.picamera2 import *
from datetime import datetime
from signal import pause
import requests
import os

pir = MotionSensor(17)
camera = Picamera2()
camera.start_preview(Preview.NULL)
config = camera.still_configuration()
camera.configure(config)

def moving():
    file_path = capture()
    upload_picture(file_path)
    cleanup(file_path)

def not_moving():
    timestamp = datetime.now().isoformat()
    print('%s All clear' % timestamp)

def capture():
    camera.start()
    timestamp = datetime.now().isoformat()
    print('%s Detected movement' % timestamp)

    file_path = '/home/pi/%s.jpg' % timestamp
    metadata = camera.capture_file(file_path)
    print(metadata)
    camera.stop()
    return file_path

def upload_picture(file_path, url = 'https://camera-server.onrender.com/upload'):
    files = {'file': open(file_path, 'rb')}
    print('Uploading file %s to URL: %s' %(file_path, url))
    r = requests.post(url, files=files)
    print (r.json())
    r.raise_for_status()

def cleanup(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print ('Removed %s' % file_path)

pir.when_motion = moving
pir.when_no_motion = not_moving

pause()
