#Imports all needed packages
import time
import RPi.GPIO as GPIO

#GPIO pin setup 1
a = 1
b = 2
c = 3
d = 4

#GPIO pin setup 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)

#Makes the robot go forward
def Forward():
    GPIO.output(a,False)
    GPIO.output(b,True)
    GPIO.output(c,False)
    GPIO.output(d,True)

#Makes the robot go in REVERSE
def Reverse():
    GPIO.output(a,True)
    GPIO.output(b,False)
    GPIO.output(c,True)
    GPIO.output(d,False)

#Turns the robot RIGHT
def TurnRight():
    GPIO.output(a,True)
    GPIO.output(b,False)
    GPIO.output(c,False)
    GPIO.output(d,True)

#Turns the robot LEFT
def TurnLeft():
    GPIO.output(a,False)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,False)

#STOPS the Robots motors completly
def Stop():
    GPIO.output(a,False)
    GPIO.output(b,False)
    GPIO.output(c,False)
    GPIO.output(d,False)

def Cleanup():
    print("Cleaning Up GPIO Pins")
    GPIO.cleanup()