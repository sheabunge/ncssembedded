from microbit import *
import radio

# this file runs on the 'slave' microbit, which will be mounted on a glove

AIR_RESISTANCE = 0.98

radio.on()
radio.config(channel=97)

speed = 0

while True:
	display.clear()
	acc = accelerometer.get_x() // 16

	if acc > 31:
		display.show(Image.ARROW_N)
		speed += acc

	radio.send(str(int(speed)))

	speed *= AIR_RESISTANCE
	sleep(20)
