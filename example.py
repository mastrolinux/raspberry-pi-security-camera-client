from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from signal import pause

pir = MotionSensor(17)
camera = PiCamera()

def capture():
    timestamp = datetime.now().isoformat()
     print('%s Detected movement' % timestamp)
    camera.capture('/home/pi/%s.jpg' % timestamp)

def not_moving():
    timestamp = datetime.now().isoformat()
    print('%s All clear' % timestamp)

pir.when_motion = capture
pir.when_no_motion = not_moving

pause()

