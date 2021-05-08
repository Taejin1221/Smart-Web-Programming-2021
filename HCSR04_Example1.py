import RPi.GPIO as GPIO
import time
from hcsr import HCSR04

triggerPin = 20
echoPin = 21

GPIO.setmode( GPIO.BCM )
sr04 = HCSR04( trigger = triggerPin, echo = echoPin )

try:
	while True:
		dist = sr04.getDistance( )
		print( 'Measured Distance = %0.1f cm' % dist )

		time.sleep( 1 )

except KeyboardInterrupt:
	print( 'Measurement stopped by User' )

finally:
	del sr04
	GPIO.cleanup()