from microbit import *
from neopixel import NeoPixel
import radio

LIGHTS = 30
MAX_SPEED = 4500

def get_light_color(pixel):
	if pixel < 8 :
		return (255, 0, 0)
	elif pixel < 16:
		return (255, 255, 0)
	elif pixel < 26:
		return (0, 255, 0)
	else:
		return (0, 0, 255)

def light_percent(np, percent):
	length = len(np)
	number_on = min(int(percent / 100 * length), length)
	np.clear()

	for pixel in range(number_on):
		np[pixel] = get_light_color(pixel)

	np.show()


radio.on()
radio.config(channel=97)
np = NeoPixel(pin0, LIGHTS)

while True:
	message = radio.receive()
	if not message:
		continue

	speed = min(int(message), MAX_SPEED) / MAX_SPEED * 100
	print(message, '->', speed)
	light_percent(np, speed)
