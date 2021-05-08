# hcsr04.py
import RPi.GPIO as GPIO
import time

class HCSR04:
	SONIC_SPEED = 34300
	def __init__( self, trigger, echo ):
		self.GPIO_TRIGGER = trigger
		self.GPIO_ECHO = echo

		GPIO.setup( self.GPIO_TRIGGER, GPIO.OUT )
		GPIO.setup( self.GPIO_ECHO, GPIO.IN )

	def getDistance( self ):
		GPIO.output( self.GPIO_TRIGGER, True )

		time.sleep( 0.00001 )
		GPIO.output( self.GPIO_TRIGGER, False )

		while ( GPIO.input( self.GPIO_ECHO ) == 0 ):
			startTime = time.time()

		while ( GPIO.input( self.GPIO_ECHO ) == 1 ):
			stopTime = time.time()

		timeElapsed = stopTime - startTime

		distance = ( timeElapsed * SONIC_SPEED ) / 2

		return distance