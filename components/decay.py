from microbit import *
import neopixel
from random import randint
start_time = 0
LEDs = 0
time = running_time()
np = neopixel.NeoPixel(pin0, 30)

update_leds = True

while True:
    time = running_time()
    if button_a.was_pressed():
        LEDs += 1
        start_time = running_time()
        
        last_button = 0
        update_leds = True
        
    elif button_b.was_pressed():
        display.scroll(str(LEDs))
    
    last_button = running_time() - start_time
    print(str(last_button))
    
    if last_button > 3000:
        update_leds = True
        LEDs -= 1
        last_button = 0
        start_time = running_time()
        
    if LEDs < 0:
        LEDs = 0
        
    if LEDs > 30:
        LEDs = 30
    
    if update_leds:
        np.clear()    
        for pixel_id in range(0, LEDs):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)
            
            np[pixel_id] = (red, green, blue)
            
        np.show()
        update_leds = False
        
    sleep(100)

