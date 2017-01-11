from microbit import *
from neopixel import NeoPixel
import radio

LIGHTS = 30
MAX_SPEED = 4500

def get_light_color(pixel):
	color_thresholds = [
		(8,  (100, 0, 0)),
		(15, (100, 100, 0)),
		(26, (0, 100, 0)),
		(30, (0, 0, 100))
	]

	for threshold, color in color_thresholds:
		if pixel <= threshold:
			return color


def light_percent(np, percent):
	length = len(np)
	number_on = min(int(percent / 100 * length), length)
	print(number_on, 'lights')

	for pixel in range(length):
		np[pixel] = get_light_color(pixel) if pixel < number_on else (0, 0, 0)
	np.show()

radio.on()
radio.config(channel=97)
np = NeoPixel(pin0, LIGHTS)

while True:
	try:
		message = radio.receive()
	except Exception as err:
		print(err)
		continue
	if not message:
		continue

	speed = min(int(message), MAX_SPEED) / MAX_SPEED * 100
	print(message, '->', speed)
	light_percent(np, speed)
