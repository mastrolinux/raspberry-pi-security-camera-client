from gpiozero import MotionSensor
from picamera2.picamera2 import *
from datetime import datetime
from signal import pause

pir = MotionSensor(17)
camera = Picamera2()
camera.start_preview(Preview.NULL)
config = camera.preview_configuration()
camera.configure(config)

def capture():
    camera.start_preview()
    camera.start()
    timestamp = datetime.now().isoformat()
    metadata = camera.capture_file('/home/pi/%s.jpg' % timestamp)
    print(metadata)
    camera.stop()

def not_moving():
	print("nothing")

pir.when_motion = capture
pir.when_no_motion = not_moving

pause()