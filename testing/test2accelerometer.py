from microbit import *
import radio
radio.on()
radio.config(channel=20)
moving_avg_speed_y = 0
x,y,z=0,0,0

def formatValue(number):
    number = int((number + 2048)//128)
    string = ("-"*number + " "*(33-number))
    return(string[:16] +"|" + string[16:])

def data_show():
    string = (formatValue(x) + formatValue(y) + formatValue(z))
    return(string)
    


while True:
    x = (accelerometer.get_x()+x)/2
    y = (accelerometer.get_x()+y)/2
    z = (accelerometer.get_x()+z)/2
    radio.send(data_show())
    print(data_show())
    sleep(50)