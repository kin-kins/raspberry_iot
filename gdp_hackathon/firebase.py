import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase
   
 
import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)

firebase = firebase.FirebaseApplication('https://spadex-e8d4a.firebaseio.com/', None)
#firebase.put("/Control", "/device1", "on")

def updatePiInfo():
	
	gas= GPIO.input(11)
	tap=GPIO.input(13)
	dust=GPIO.input(15)
	firebase.put("/Control", "/device1", "off")
	
	firebase.put('/Control', '/gas',gas)
	firebase.put('/Control', '/tap',tap)
	firebase.put('/Control', '/dust',dust)
	'''temp=firebase.get('/Control', '/temp')
	humid=firebase.get('/Control', '/humid')
	print result
	
	if ( result == "on" ): 	  		
		print "Lights on" 
		GPIO.output(18,GPIO.HIGH)
	else :
		if ( result == "off" ):
			print "Lights off"
			GPIO.output(18,GPIO.LOW)'''


#firebase.post("/Control/device1", "off")
firebase.put("/Control", "/device1", "off")

while True:
	updatePiInfo()
	#firebase.put("/Control", "/device1", "off")
		
        #Retrieve sleep time from firebase and continue the loop
        #sleepTime = firebase.get("/Settings/info_update_time_interval", None)
        #sleepTime = int(sleepTime)
	sleep(1)
