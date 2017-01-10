from microbit import *
from neopixel import NeoPixel


LIGHTS = 30
COLORS = [(0, 255, 0)] * LIGHTS

def light_percent(np, percent, colors):
	length = len(np)
	number_on = min(int(percent / 100 * length), length)
	np.clear()

	for pixel in range(number_on):
		np[pixel] = colors[pixel]
	np.show()

np = NeoPixel(pin0, LIGHTS)

for i in range(100):
	light_percent(np, i + 1, COLORS)
	sleep(200)
