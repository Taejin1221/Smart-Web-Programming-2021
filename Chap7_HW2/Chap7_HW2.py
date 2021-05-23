# Chap7_HW2.py
import board
import busio
import Adafruit_BMP.BMP085 as BMP085

from flask import Flask, render_template

app = Flask( __name__ )

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
# bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bmp180 = BMP085.BMP085( )

@app.route( '/temperature' )
def index():
	return render_template( 'index.html',
		temperature = bmp180.read_temperature(),
		pressure = bmp180.read_sealevel_pressure(),
		altitude = bmp180.read_altitude()
	)

if __name__ == '__main__':
	app.run( host='0.0.0.0' )