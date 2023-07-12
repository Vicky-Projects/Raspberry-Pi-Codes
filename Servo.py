
import RPi.GPIO as GPIO
import time

from time import sleep
duty=2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
pwm=GPIO.PWM(33, 50)
pwm.start(2.5)
def SetAngle(angle):
	duty = angle / 18+2
	GPIO.output(33, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(2)
	GPIO.output(33, False)
	pwm.ChangeDutyCycle(0)

while True:
        for i in range(0,255,1):
                SetAngle(i)
                time.sleep(0.5)
	
pwm.stop()
GPIO.cleanup()
 
