from gpiozero import MotionSensor
from picamera2.picamera2 import *
from datetime import datetime
from signal import pause

pir = MotionSensor(17)
camera = Picamera2()
camera.start_preview(Preview.NULL)
config = camera.still_configuration()
camera.configure(config)

def capture():
    camera.start()
    timestamp = datetime.now().isoformat()
    print('%s Detected movement' % timestamp)

    metadata = camera.capture_file('/home/pi/%s.jpg' % timestamp)
    print(metadata)
    camera.stop()

def not_moving():
    timestamp = datetime.now().isoformat()
    print('%s All clear' % timestamp)

pir.when_motion = capture
pir.when_no_motion = not_moving

pause()
