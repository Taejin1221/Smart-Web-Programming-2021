# Chap6_HW.py
import time, Adafruit_SSD1306, hcsr04
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

TOP = -2
Padding = 2

RST = None

disp = Adafruit_SSD1306.SSD1306_128_64( rst = RST )
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height
frame = Image.new( '1', ( WIDTH, HEIGHT ) )

draw = ImageDraw.Draw( frame )
font = ImageFont.load_default()
disp.clear( )

triggerPin = 20
echoPin = 21

GPIO.setmode( GPIO.BCM )
sr04 = hcsr04.HCSR04( trigger = triggerPin, echo = echoPin )

try:
    while True:
        dist = sr04.getDistance( )

        draw.rectangle( ( 0, 0, WIDTH, HEIGHT ), outline = 0, fill = 0 )

        draw.text( ( Padding, TOP), 'Distance(cm)', font = font, fill = 255 )
        draw.text( ( Padding, TOP + 16), '{:.2f}'.format( dist ), font = font, fill = 255 )
        

        disp.image( frame )
        disp.display()
        time.sleep( 0.1 )
except KeyboardInterrupt:
    disp.clear()
    disp.display()
finally:
    del sr04
    GPIO.cleanup()

    print( 'Bye...' )