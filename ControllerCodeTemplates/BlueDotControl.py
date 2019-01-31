from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO
import time

def dpad(pos):
    if pos.top:
        
    elif pos.bottom:
        
    elif pos.left:
        
    elif pos.right:
        
    elif pos.middle:
        
bd = BlueDot()
bd.when_pressed = dpad