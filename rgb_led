
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3 ,GPIO.OUT)
GPIO.setup(5 ,GPIO.OUT)
GPIO.setup(7 ,GPIO.OUT)

while (True):
        request=raw_input("rgb")
        if(len(request)==3):
                print "hh"
                GPIO.output(3 ,int(request[0]))
                GPIO.output(5 ,int(request[1]))
                GPIO.output(7 ,int(request[2]))
