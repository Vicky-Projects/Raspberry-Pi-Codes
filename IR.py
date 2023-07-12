import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(35, IO.OUT)
IO.setup(37, IO.IN)
IO.output(35, False)
while 1:
    if(IO.input(37)==True):
        IO.output(35, True)
    else:
        IO.output(35, False)
