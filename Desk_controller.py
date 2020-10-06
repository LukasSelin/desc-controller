import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
    
upPort = 29
downPart = 31
controllPort = 33
maxHight = 650
currentHight = maxHight

def initPorts():
    GPIO.setup(upPort, GPIO.OUT)
    GPIO.setup(downPart, GPIO.OUT)
    GPIO.setup(controllPort, GPIO.OUT)

def calibrate():
    print("Started calibrating")
    GPIO.output(upPort, 1)
    GPIO.output(controllPort, 1)

    time.sleep(20)

    GPIO.output(upPort, 0)
    GPIO.output(controllPort, 0)
    print("Calibrate complete")


def moveUp(offsetSeconds):
    print("Moving up for {} seconds".format(offsetSeconds))
    GPIO.output(upPort, 1)
    GPIO.output(controllPort, 1)

    time.sleep(offsetSeconds)
    
    GPIO.output(upPort, 0)
    GPIO.output(controllPort, 0)
    print("Stopped going up")

def moveDown(offsetSeconds):
    print("Moving down for {} seconds".format(offsetSeconds))
    GPIO.output(downPart, 1)
    GPIO.output(controllPort, 1)
    offsetSeconds = offsetSeconds * -1

    time.sleep(offsetSeconds)
    
    GPIO.output(downPart, 0)
    GPIO.output(controllPort, 0)
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
    desiredHight = 250
    offsetHight = desiredHight - currentHight
    currentHight = move(offsetHight)
    print("Current hight: {} ".format(currentHight))
    desiredHight = 450
    offsetHight = desiredHight - currentHight
    currentHight = move(offsetHight)
    print("Current hight: {} ".format(currentHight))

