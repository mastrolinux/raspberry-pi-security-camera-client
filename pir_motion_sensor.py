from gpiozero import MotionSensor
from datetime import datetime
from signal import pause

pir = MotionSensor(17)

### I suggest it to tune it at about 7-10 seconds
### The time potentiometer should be turned 
### Counterclockwise at almost horizontally
### https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/testing-a-pir

def capture():
    timestamp = datetime.now().isoformat()
    print('%s Detected movement' % timestamp)

def not_moving():
    timestamp = datetime.now().isoformat()
    print('%s All clear' % timestamp)

pir.when_motion = capture
pir.when_no_motion = not_moving

pause()