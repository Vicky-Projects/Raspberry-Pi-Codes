import RPi.GPIO as GPIO
import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



gpio=17

while True:
    humidity,temperature = Adafruit_DHT.read_retry(sensor,gpio)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature,humidity))
else:
    print('Failed.Try again!')
