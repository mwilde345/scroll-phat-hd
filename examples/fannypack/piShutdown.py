from gpiozero import Button
import time
import os

stopButton = Button(26)

while True:
	if stopButton.is_pressed:
		time.sleep(1)
		if stopButton.is_pressed:
			os.system("shutdown now -h")
	time.sleep(1)
