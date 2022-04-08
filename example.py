from gpiozero import MotionSensor
# from picamera import PiCamera
from datetime import datetime
from signal import pause

pir = MotionSensor(17)
# camera = PiCamera()

def capture():
    timestamp = datetime.now().isoformat()
    print('/home/pi/%s.jpg' % timestamp)
    # camera.capture('/home/pi/%s.jpg' % timestamp)

def not_moving():
	print("nothing")

pir.when_motion = capture
pir.when_no_motion = not_moving

pause()

