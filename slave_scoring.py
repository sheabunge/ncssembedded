from microbit import *
import radio

radio.on()

while True:
    display.clear()
    if accelerometer.get_x() > 500:
        print("scoring")
        radio.send()
        display.show(Image.ARROW_N)
    
    sleep(20)