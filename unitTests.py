from ClassConfig import *
from gpio_lcd import GpioLcd
from time import sleep_ms

hardware = Hardware()



hardware.software.speed = 500
print("LED ShowSequence test")
hardware.ShowSequence([0 ,3 ,1 ,2])
sleep_ms(1500)
hardware.ShowSequence([2, 1, 3, 0])

print("Hardware GetSequence test, press the buttons left to right")
hardware.software.sequence = [2, 1, 3, 0]
hardware.GetSequence()

print("Generate sequence")
hardware.software.GenerateSequence()
print(hardware.software.sequence)