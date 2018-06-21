import RPi.GPIO as GPIO
import time
import smtplib
msg="it works"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("YOUR GMAIL ID", "YOUR PASSWORD")
GPIO.setmode(GPIO.BCM);
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(17,GPIO.IN)
msg = "motion detection recieved " 
print("Here we go! Press CTRL+C to exit")
try:
    while True :
        if (GPIO.input(butPin)):
            GPIO.output(ledPin,HIGH)
            server.sendmail("spadetch@gmail.com", "k.ashu403@gmail.com", msg)  
            else:
            GPIO.output(ledPin,GPIO.LOW)
except KeyboardInterrupt:
    print ("keyboard Interrupt") # If CTRL+C is pressed, exit cleanly:
    server.quit()
    GPIO.cleanup()

            
