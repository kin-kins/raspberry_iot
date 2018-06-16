import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p=GPIO.PWM(11,100)
p.start(0)
while True:
    #GPIO.output(11,GPIO.HIGH)
    print ("high")
    for x in range(100):
                p.ChangeDutyCycle(x)
                time.sleep(0.1)

    #GPIO.output(11,GPIO.LOW)
    time.sleep(1)
    print ("low")
