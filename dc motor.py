import RPi.GPIO as GPIO
import time

# Motor control pins
motorPin1 = 27  # GPIO pin for motor control (Input 1)
motorPin2 = 22  # GPIO pin for motor control (Input 2)
enablePin = 17  # GPIO pin for motor control (Enable)

# Encoder pins
encoderPin1 = 2  # GPIO pin for encoder A
encoderPin2 = 3  # GPIO pin for encoder B

# PID parameters
Kp = 1.0  # Proportional gain
Ki = 0.1  # Integral gain
Kd = 0.1  # Derivative gain

# Target position and initial variables
targetPosition = 0  # Target position for the motor
encoderCount = 0  # Current encoder count
previousEncoderCount = 0  # Previous encoder count
integralError = 0  # Integral of error for PID control
previousTime = 0  # Previous time for calculating time difference

# Motor control variables
motorSpeed = 0  # Motor speed (PWM duty cycle)

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin1, GPIO.OUT)
GPIO.setup(motorPin2, GPIO.OUT)
GPIO.setup(enablePin, GPIO.OUT)
GPIO.setup(encoderPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoderPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setwarnings(False)
# Create PWM object for motor speed control
pwm = GPIO.PWM(enablePin, 100)  # Frequency: 100 Hz

def calculatePID():
    global encoderCount, previousEncoderCount, integralError, previousTime, motorSpeed

    currentTime = time.time()
    deltaTime = currentTime - previousTime
    previousTime = currentTime

    # Calculate the error between the current and target position
    error = targetPosition - encoderCount

    # Calculate the PID control signal
    proportional = Kp * error
    integralError += Ki * error * deltaTime
    derivative = Kd * (encoderCount - previousEncoderCount) / deltaTime

    controlSignal = proportional + integralError + derivative

    # Update the motor speed based on the control signal
    motorSpeed = abs(int(controlSignal))
    if motorSpeed > 100:
        motorSpeed = 100

    previousEncoderCount = encoderCount


def updateMotor():
    # Update the motor speed and direction
    if motorSpeed == 0:
        GPIO.output(motorPin1, GPIO.LOW)
        GPIO.output(motorPin2, GPIO.LOW)
    else:
        if targetPosition > encoderCount:
            GPIO.output(motorPin1, GPIO.HIGH)
            GPIO.output(motorPin2, GPIO.LOW)
        else:
            GPIO.output(motorPin1, GPIO.LOW)
            GPIO.output(motorPin2, GPIO.HIGH)
    
    pwm.ChangeDutyCycle(motorSpeed)

def encoderCallback(channel):
    global encoderCount, previousEncoderCount

    # Read the current state of encoder pins
    pin1State = GPIO.input(encoderPin1)
    pin2State = GPIO.input(encoderPin2)

    # Update the encoder count based on the state change of encoder pins
    if pin1State == pin2State:
        encoderCount += 1
    else:
        encoderCount -= 1

    previousEncoderCount = encoderCount


# Attach interrupt for the encoder pin
GPIO.add_event_detect(encoderPin1, GPIO.BOTH, callback=encoderCallback)

try:
    pwm.start(0)  # Start PWM with 0% duty cycle
    while True:
        calculatePID()
        updateMotor()
        time.sleep(0.01)  # Adjust the delay time as needed for your application

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
