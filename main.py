from ClassConfig import *
from gpio_lcd import GpioLcd

software = Software()
hardware = Hardware()

sequence = []
playerSeq = []
level = 1
note = 0
speed = 1050

<<<<<<< HEAD
sequence = software.GenerateSequence()
=======
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

#while resetButton.value() == False:
    #lcd.putstr("Press Start")
    

software.GenerateSequence()
hardware.ShowSequence(sequence)
hardware.GetSequence()
software.GenerateSequence()
hardware.ShowSequence(sequence)
hardware.GetSequence()
software.GenerateSequence()
hardware.ShowSequence(sequence)
hardware.GetSequence()
software.GenerateSequence()
>>>>>>> 4878003b9988f214c41dbef1e75ddfc41884aaa1
hardware.ShowSequence(sequence)
hardware.GetSequence()

