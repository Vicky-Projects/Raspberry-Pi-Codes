
import RPi.GPIO as GPIO
import time
DU = [4,5,6,7,8,9,10]
from time import sleep
duty=2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
pwm=GPIO.PWM(33, 50)
pwm.start(0)
while True:
    for i in range(7):
        pwm.ChangeDutyCycle(DU[i])
        time.sleep(1)
        print(i)
        

