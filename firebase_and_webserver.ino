import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
import time
import datetime
GPIO.setmode(GPIO.BCM)
import urllib2, urllib, httplib
import json
import os 
from functools import partial
# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)
firebase = firebase.FirebaseApplication('https://YOUR-FIREBASE-URL.firebaseio.com', None)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      firebase.put("/Control", "/device1", "on")
      #GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      firebase.put("/Control", "/device1", "off")
      #GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   result = firebase.get('/Control', '/device1')
   print result
   
   if ( result == "on" ): 	  		
       print "Lights on" 
       GPIO.output(18,GPIO.HIGH)
   else :
       if ( result == "off" ):
           print "Lights off"
           GPIO.output(18,GPIO.LOW)
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   firebase.put("/Control", "/device1", "off")

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
