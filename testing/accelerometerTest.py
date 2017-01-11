from microbit import *
import music
"""class microBitButton():

  def __init__(self,buttonthing):
    self.b = buttonthing
    self.pressed = False
    self.wasreleased = False
  
  def update_was_released(self):
    if self.b.was_pressed(): self.pressed = True
    if self.pressed and not self.b.is_pressed():
      self.pressed = False
      self.wasreleased = True
      
  def was_released(self):
    if self.wasreleased :
      self.wasreleased = False
      return True
    else:
      return False


x = 0
y = 0
a = microBitButton(button_a)
b = microBitButton(button_b)



"""
import radio
radio.on()
radio.config(channel=20)

def formatValue(number):
    number = (number + 2048)//128
    string = ("-"*number + " "*(33-number))
    return(string[:16] +"|" + string[16:])

def data_show():
    print(formatValue(accelerometer.get_x()) + formatValue(accelerometer.get_y()) + formatValue(accelerometer.get_z()))


while True:
    message = radio.receive()
    if message == "1":
        data_show()
    elif message == "0":
        print("stop")
    sleep(50)
        
        
    #if button_a.was_pressed():
    #    print("start")
    #if button_a.is_pressed():
    #    data_show()