import RPi.GPIO as GPIO             
import time
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         
GPIO.setup(3, GPIO.OUT)    



while True:
	i=GPIO.input(11)
	if i==0:                 #When everything is quiet monitor mode
		print ('OK')
	elif i==1: 
		print ('Houseparty') #When someone is detected,Apollo reacts with process generation
		subprocess.call (["process.exit()"])

		