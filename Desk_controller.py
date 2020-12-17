import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


upPort = 29
downPart = 31
controllPort = 33
pwmPort = 12
maxHight = 650
currentHight = maxHight
# baksidan av el kabeln

def initPorts():
    GPIO.setup(upPort, GPIO.IN)
    GPIO.setup(downPart, GPIO.IN)
    GPIO.setup(controllPort, GPIO.OUT)
    
 #   GPIO.setup(controllPort, GPIO.OUT, initial=GPIO.LOW)

def calibrate():
    print("Started calibrating")
    moveUp(20)
    print("Calibrate complete")


def moveUp(offsetSeconds):
    print("Moving up for {} seconds".format(offsetSeconds))
    GPIO.output(controllPort, GPIO.input(upPort))

    #GPIO.output(controllPort, 1)

    time.sleep(offsetSeconds)
    
    GPIO.output(controllPort, 0)
    #GPIO.output(controllPort, 0)
    print("Stopped going up")

def moveDown(offsetSeconds):
    print("Moving down for {} seconds".format(offsetSeconds))
    GPIO.output(controllPort, GPIO.input(downPart))

    #GPIO.output(controllPort, 1)
    offsetSeconds = offsetSeconds * -1

    time.sleep(offsetSeconds)
    
    GPIO.output(downPart, 0)
    #GPIO.output(controllPort, 0)
    print("Stopped going down")

def move(offsetHight):

    offsetSeconds = offsetHight / 35

    if 0 < offsetHight:
        moveUp(offsetSeconds)
    else:
        moveDown(offsetSeconds)
    return offsetHight
    

initPorts()
calibrate()
currentHight = maxHight

while(True):
    moveUp(5)
    moveDown(5)

