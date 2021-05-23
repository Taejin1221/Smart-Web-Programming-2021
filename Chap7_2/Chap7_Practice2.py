# Chap7_Practice2.py
import RPi.GPIO as GPIO
from flask import Flask

app = Flask( __name__ )

led_pin = 18
GPIO.setmode( GPIO.BCM )
GPIO.setup( led_pin, GPIO.OUT )

@app.route( '/' )
def hello():
	return '<font size=10> Hello, LED! </font>'

@app.route( '/led/on' )
def led_on( ):
	GPIO.output( led_pin, GPIO.HIGH )
	return '<font size=10> LED {} ON! </font>'.format( led_pin )

@app.route( '/led/off' )
def led_off( ):
	GPIO.output( led_pin, GPIO.LOW )
	return '<font size=10> LED {} OFF! </font>'.format( led_pin )

if __name__ == '__main__':
	app.run( host = '0.0.0.0' )