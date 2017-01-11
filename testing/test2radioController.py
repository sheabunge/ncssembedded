from microbit import *
import radio

radio.on()
radio.config(channel=20)

while True:
    message = radio.receive()
    if message:
        
        print(message) #running_time
    