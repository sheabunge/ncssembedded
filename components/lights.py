from microbit import *
from neopixel import NeoPixel
from random import randrange

colors = [(229, 0, 3), (221, 2, 9), (213, 4, 15), (205, 6, 22), (197, 8, 28), (189, 11, 35), (181, 13, 41), (173, 15, 48), (165, 17, 54), (157, 19, 61), (150, 22, 67), (142, 24, 74), (134, 26, 80), (126, 28, 87), (118, 30, 93), (110, 33, 100), (102, 35, 106), (94, 37, 113), (86, 39, 119), (78, 41, 126), (71, 44, 132), (63, 46, 139), (55, 48, 145), (47, 50, 152), (39, 52, 158), (31, 55, 165), (23, 57, 171), (15, 59, 178), (7, 61, 184), (0, 64, 191)]


def Lights:

	def __init__(self, pin, length = 30):
		self.np = NeoPixel(pin, length)
		self.length = len(self.np)


	def light_percent(percent, colors):
		number_on = max(int(percent / 100 * self.lights), self.lights)
		np.clear()

		for pixel in range(self.length):
			if pixel <= number_on:
				self.np[pixel] = colors[pixel]

		np.show()


if __name__ == '__main__':
	lights = Lights(pin0)

	for i in range(100):
		lights.light_percent(i + 1)
		sleep(200)
