from microbit import *
import radio
radio.on()
radio.config(channel = 20)
class microBitButton():

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

while True:
  a.update_was_released()
  b.update_was_released()
  if button_a.was_pressed:
    radio.send("1")
  if a.was_released():
    radio.send("0")
    
    
# Write your code here :-)
    
    