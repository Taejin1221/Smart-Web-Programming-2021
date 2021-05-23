# Chap7_HW2.py
import time
import board
import busio
import adafruit_bme280

from flask import Flask, render_template

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1013.25

@app.route( '/temperature' )
def index():
	return render_template( 'index.html',
		temperature = bme280.temperature,
		humidity = bme280.humidity,
		pressure = bme280.pressure,
		altitude = bme280.altitude
	)