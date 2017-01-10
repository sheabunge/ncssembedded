from microbit import *
import radio
AIR_RESISTANCE = 0.98
radio.on()
radio.config(channel=20)
speed = 0
while True:
    display.clear()
    acc = accelerometer.get_x()//16
    if acc > 31:
        display.show(Image.ARROW_N)
        speed += acc
    sleep(20)
    radio.send(str(int(speed)))
    speed *= AIR_RESISTANCE
    
    
   