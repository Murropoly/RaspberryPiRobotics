'''
This is a module made for the L298N
Made by Tyler Muranaka
'''
#Imports all needed packages
import RPi.GPIO as GPIO
import time

#GPIO pin setup 1
a = 7
b = 8
c = 9
d = 10

#GPIO pin setup 2
GPIO.setmode(GPIO.BOARD)
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
    GPIO.cleanup()