# !/bin/python

# Simple script for shutting down the Raspberry Pi at the press of a button.

# by mitesh
import RPi.GPIO as GPIO
import time
import os
# Use the Broadcom SOC Pin numbers

# Setup the pin with internal pullups enabled and pin in reading mode.

# FIRST CHECK PIN INDEX SEE THE PIN GROUP 

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    messageBox.showinfo("System Going Down....")
    #print("Shutting Down")
    time.sleep(5)
    os.system("killall -e rdesktop")
    os.system("sudo shutdown -h now")
 
 # Add our function to execute when the button pressed event happens

GPIO.add_event_detect(5, GPIO.FALLING, callback=Shutdown, bouncetime=2000)
# Now wait!
while 1:
    time.sleep(1)
