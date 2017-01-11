from microbit import *
import radio
AIR_RESISTANCE = 0.98
radio.on()
radio.config(channel=97)
speed = 0
start = 0
positive_acc = False
min_speed_y = 0
speedbuffer = 0
cycles = 0
def handicap(base, val,threshold):
    return val * min(1,(base/threshold)**3)
    
while True:
    
    cycles += 1
    
    display.clear()
    acc = accelerometer.get_x()//16
    
    #init swing
    #set mode, initiate timer, initiate buffer
    if acc > 31 and not positive_acc:
        
        positive_acc = True
        start = running_time()
        speedbuffer = 0
    #continue swing
    #add to buffer
    if acc > 31 and positive_acc:
        display.show(Image.ARROW_N)
        min_speed_y = min(min_speed_y,accelerometer.get_y())
        speedbuffer += acc
        
    #end swing
    #set mode, add buffer to main val, read from timer
    if acc < 31 and positive_acc:
        positive_acc = False
        speed += handicap(4096-(min_speed_y+2048),handicap(running_time()-start,speedbuffer,130),4048)
        print(speed,running_time()-start,speedbuffer)
        min_speed_y = 0
   # print(speed)
    if cycles %5 == 0:
        radio.send(str(int(speed)))
    speed *= AIR_RESISTANCE
    sleep(20)
    
    