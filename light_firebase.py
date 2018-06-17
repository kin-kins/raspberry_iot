import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase


import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

firebase = firebase.FirebaseApplication('https://YOUR-FIREBASE-URL.firebaseio.com', None)
#firebase.put("/Control", "/device1", "on")

def updatePiInfo():
	result = firebase.get('/Control', '/device1')
	print result
	
	if ( result == "on" ): 	  		
		print "Lights on" 
		GPIO.output(18,GPIO.HIGH)
	else :
		if ( result == "off" ):
			print "Lights off"
			GPIO.output(18,GPIO.LOW)


#firebase.post("/Control/device1", "off")
firebase.put("/Control", "/device1", "off")

while True:
	updatePiInfo()
	#firebase.put("/Control", "/device1", "off")
		
        #Retrieve sleep time from firebase and continue the loop
        #sleepTime = firebase.get("/Settings/info_update_time_interval", None)
        #sleepTime = int(sleepTime)
	sleep(1)
