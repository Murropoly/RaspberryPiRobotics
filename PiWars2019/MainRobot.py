import RPiRobot
from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO
import time

bd = BlueDot()
Forward() = RPiRobot.Forward()
Reverse() = RPiRobot.Reverse()
TurnRight() = RPiRobot.TurnRight()
TurnLeft() = RPiRobot.TurnLeft()
Stop() = RPiRobot.Stop()

def move(pos):
    if pos.top:
        Forward()
    elif pos.bottom:
        Reverse()
    elif pos.left:
        TurnRight()
    elif pos.right:
        TurnLeft()
    elif pos.middle:
        
def stop():
    RPiRobot.Cleanup()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop