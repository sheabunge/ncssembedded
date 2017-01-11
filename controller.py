from microbit import *
from neopixel import NeoPixel
import radio

LIGHTS = 30
MAX_SPEED = 3500
SCORE_THRESHOLD = 50

color_thresholds = [
	(7,  (100, 0, 0)),
	(8,  (75, 10, 0)),
	(9,  (75, 30, 0)),
	(10, (75, 50, 0)),

	(11, (50, 75, 0)),
	(12, (50, 75, 0)),
	(14, (50, 100, 0)),

	(17, (0, 100, 0)),
	(25, (0, 100, 10)),
	(26, (0, 100, 50)),
	(27, (0, 75, 100)),
	(30, (0, 0, 100))
]

def get_light_color(pixel):
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


def format_score(milliseconds):
	seconds = milliseconds // 1000
	return '{:d}s'.format(seconds)

radio.on()
radio.config(channel=97)
np = NeoPixel(pin0, LIGHTS)

best_time = 0
start_time = 0
moving_average = 0

while True:
	try:
		message = radio.receive()
	except Exception as err:
		print(err)
		continue
	if not message:
		continue

	speed = min(int(message), MAX_SPEED)
	moving_average = moving_average * .4 + speed * .6

	percentage = moving_average / MAX_SPEED * 100
	kmh = percentage * 50
	print('travelling at', kmh, 'km/h')

	if moving_average != 0.0:
		print(message, '->', moving_average)
		light_percent(np, percentage)

	if speed > SCORE_THRESHOLD and start_time == -1:
		start_time = running_time()

	if speed < SCORE_THRESHOLD and start_time != -1:
		score = running_time() - start_time
		best_time = max(score, best_time)
		start_time = -1
		display.scroll(format_score(best_time), wait=False, loop=True)

	if start_time != -1:
		print('time: ' + format_score(score))
		print('best time: ' + format_score(best_time))
