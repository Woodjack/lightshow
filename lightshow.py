import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library. Allows us to use 'sleep'
from stepMotorControl import stepperMotor

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(5, GPIO.OUT) ## Setup GPIO pin 5 to OUT
GPIO.setup(3, GPIO.OUT) ## Setup GPIO pin 3 to OUT



def on():
	GPIO.output(3, 1)
	GPIO.output(5, 1)

def off():
	GPIO.output(3, 0)
	GPIO.output(3, 0)