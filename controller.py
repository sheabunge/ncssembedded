from microbit import *
from neopixel import NeoPixel
import radio

# this code will run on the 'master' microbit which manages the lights, etc

LIGHTS = 30
COLORS = [(255, 0, 0)] * 9 + [(0, 0, 255)] * 10 + [(0, 255, 0)] * 11


def light_percent(np, percent, colors):
	length = len(np)
	number_on = min(int(percent / 100 * length), length)
	print('turning', number_on, 'lights on')
	np.clear()

	for pixel in range(number_on):
		np[pixel] = colors[pixel]
	np.show()


radio.on()
radio.config(channel=97)
np = NeoPixel(pin0, LIGHTS)

while True:
	message = radio.receive()
	if not message:
		continue

	speed = int(message) // 400
	print(speed)
	light_percent(np, speed, COLORS)
