import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

p=GPIO.PWM(33, 50)
p.start(0)

while(1):
    for i in range(0,101,20):
        p.ChangeDutyCycle(i)
        time.sleep(0.5)
    for i in range(100,0,-20):
        p.ChangeDutyCycle(i)
        time.sleep(0.5)
