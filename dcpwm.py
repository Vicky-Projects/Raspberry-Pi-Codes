import RPi.GPIO as GPIO
import time



float eintegral = 0
float RPM
volatile long encodercount=0,lastcount
unsigned long lasttime,now
float prevT,currentT

#define encoder pins
ENCA 3
ENCB 5

pos = 0


# Motor control pins
motorPin1 = 35  # GPIO pin for motor control (Input 1)
motorPin2 = 37  # GPIO pin for motor control (Input 2)
en = 33  # GPIO pin for motor control (Enable)




#set GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(encoderPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoderPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(motorPin1, GPIO.OUT)
GPIO.setup(motorPin2, GPIO.OUT)


GPIO.setup(33, GPIO.OUT)
pwm=GPIO.PWM(33, 50)
pwm.start(0)
def setmotor(dire, pwmval, pwm,motorPin1,motorPin2):
    if dire == 0:
        GPIO.output(motorPin1, GPIO.LOW)
        GPIO.output(motorPin2, GPIO.LOW)
    else:
        if targetPosition > encoderCount:
            GPIO.output(motorPin1, GPIO.HIGH)
            GPIO.output(motorPin2, GPIO.LOW)
        else:
            GPIO.output(motorPin1, GPIO.LOW)
            GPIO.output(motorPin2, GPIO.HIGH)
