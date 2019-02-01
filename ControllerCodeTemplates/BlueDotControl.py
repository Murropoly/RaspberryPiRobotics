from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO

bd = BlueDot()

def move(pos):
    if pos.top:
        
    elif pos.bottom:
        
    elif pos.left:
        
    elif pos.right:
        
    elif pos.middle:
        
def stop():
      
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop