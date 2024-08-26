from machine import Pin
from gpio_lcd import GpioLcd
import utime

#Configure the Gpio pin of the Raspberry pi pico
lcd = GpioLcd(rs_pin = Pin(3),
              enable_pin = Pin(2),
              d0_pin = Pin(11),
              d1_pin = Pin(10),
              d2_pin = Pin(9),
              d3_pin = Pin(8),
              d4_pin = Pin(7),
              d5_pin = Pin(6),
              d6_pin = Pin(5),
              d7_pin = Pin(4),
              num_lines = 2, num_columns = 16)
#print the string on the display
lcd.putstr('Press Start To  Play Again')


