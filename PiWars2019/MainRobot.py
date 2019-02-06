from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO
import RPiRobot

bd = BlueDot()

def move(pos):
    if pos.top:
        RPiRobot.Forward()
    elif pos.bottom:
        RPiRobot.Reverse()
    elif pos.left:
        RPiRobot.TurnLeft()
    elif pos.right:
        RPiRobot.TurnRight()
    elif pos.middle:
        RPiRobot.Cleanup()
        
def stop():
    RPiRobot.Stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop