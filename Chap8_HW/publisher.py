# publisher.py
import paho.mqtt.client as mqtt
import time
import Adafruit_BMP.BMP085 as BMP085

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_publish(client, userdata, result):
    print("data published")

def on_log(client, userdata, level, buf):
    print('log: ' + buf)

pub1 = mqtt.Client('mqtt_client1', transport = 'websockets')
pub1.tls_set()
pub1.connect("test.mosquitto.org", port = 8081)

pub1.on_connect = on_connect
pub1.on_publish = on_publish
pub1.on_log = on_log

sensor = BMP085.BMP085()

try:
    while True:
        pub1.publish("SmartWebProgramming/Chap8", str(sensor.read_temperature()))
        pub1.loop()
        time.sleep(3)
except KeyboardInterrupt:
    print('bye...')
finally:
    pub1.loop_stop()
    pub1.disconnect()