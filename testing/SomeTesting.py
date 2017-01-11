from microbit import *
import radio
AIR_RESISTANCE = 0.98
radio.on()
radio.config(channel=20)
speed = 0
while True:
 #   display.clear()
    acc = accelerometer.get_x()
    
    if(acc > 0):
        start = running_time()
        while acc > 0:
            acc = accelerometer.get_x()
            pass
        radio.send(str(running_time()-start))
    sleep(20)
    #radio.send(str(int()))
    speed *= AIR_RESISTANCE
   