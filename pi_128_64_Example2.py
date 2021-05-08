# pi_128_64_Example2.py
import time
import Adafruit_SSD1306
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
font = ImageFont.load_default( )
disp.clear( )

try:
    while True:
        draw.text( ( Padding, TOP), 'Hello', font = font, fill = 255 )
        draw.text( ( Padding, TOP + 16), 'World!', font = font, fill = 255 )

        disp.image( frame )
        disp.display()
        time.sleep( 1 )
except KeyboardInterrupt:
    disp.clear()
    disp.display()
finally:
    print( 'Bye...' )