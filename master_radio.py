from microbit import *
import radio

radio.on()
radio.config(channel=20)

maximum = 0

while True:
    message = radio.receive()
    if message:
        speed = int(message)//400
        if speed > maximum:
            maximum = speed
            print("Maximum:", maximum)
        print(message) #running_time
    