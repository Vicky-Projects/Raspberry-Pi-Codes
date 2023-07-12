import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 3
ECHO = 5

print("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
pulse_start=0
pulse_end=0
while True:
    GPIO.output(TRIG,GPIO.LOW)
    print("wait for sensor")
    time.sleep(2)
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG,GPIO.LOW)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_dur = pulse_end - pulse_start

    distance = pulse_dur * 17150
    distance = round(distance, 2)
    print(f"Distance: {distance} cm")
GPIO.cleanup()
    
    
