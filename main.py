from gpiozero import MotionSensor
from picamera2.picamera2 import *
from datetime import datetime
from signal import pause
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
import json


load_dotenv()
settings = {}
settings['PIR_GPIO'] = int(os.getenv('PIR_GPIO', 17))
settings['SERVER'] = { 
    'user': os.getenv('USERNAME'), 
    'password': os.getenv('PASSWORD'),
    'base_url': os.getenv('API_SERVER')
    }

settings['IMG_PATH'] = os.getenv('IMG_PATH', 'img')

def setup_path(path):
    try:
        os.mkdir(path)
        print("Directory ", path, " Created ") 
    except FileExistsError:
        print("Directory ", path, " already exists")


def setup_camera():
    camera = Picamera2()
    camera.start_preview(Preview.NULL)
    config = camera.still_configuration()
    camera.configure(config)
    return camera


def picture_when_motion(pir, camera, settings):
    setup_path(settings.get('IMG_PATH'))
    def capture_and_upload_picture():
        if camera:
            file_path = capture(camera, settings.get('IMG_PATH'))
            server_settings = settings.get('SERVER')
            uploaded = upload_picture(file_path, server_settings)
            if uploaded:
                cleanup(file_path)
        else:
            print("Camera not defined")
    return capture_and_upload_picture

def not_moving():
    timestamp = datetime.now().isoformat()
    print('%s All clear' % timestamp)

def capture(camera, path='/home/pi/'):
    camera.start()
    timestamp = datetime.now().isoformat(timespec='seconds')
    print('%s Detected movement' % timestamp)

    file_path = os.path.join(path, '%s.jpg' % timestamp)
    metadata = camera.capture_file(file_path)
    print(metadata)
    camera.stop()
    return file_path

def upload_picture(file_path, server_settings):
    if server_settings.get('base_url'):
        url = urljoin(server_settings.get('base_url'), 'upload')
    if server_settings.get('user') and server_settings.get('password'):
        user = server_settings.get('user')
        password = server_settings.get('password')

    files = {'file': open(file_path, 'rb')}
    print('Uploading file %s to URL: %s' %(file_path, url))
    try:
        r = requests.post(url, files=files, auth=HTTPBasicAuth(user, password))
    except e:
        print(e)
    image_path = r.json().get('path')
    if not image_path or not r.ok:
        print('Error uploading image')
        return False
    print('Image available at: {}'.format(image_path))
    return True
    

def cleanup(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print ('Removed %s' % file_path)

def init(settings):
    camera = setup_camera()
    pir = MotionSensor(settings.get('PIR_GPIO'))
    pir.when_motion = picture_when_motion(pir, camera, settings)
    pir.when_no_motion = not_moving
    pause()

if __name__ == '__main__': 
    init(settings)