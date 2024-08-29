from ClassConfig import *
from gpio_lcd import GpioLcd

hardware = Hardware()

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

def Start():
    lcd.putstr("Press Start")
    hardware.software.lose = False
    while resetButton.value() == False:
        sleep_ms(50)    
    lcd.clear()
    hardware.software.speed = 200
    hardware.ShowSequence([0, 3, 1, 2, 1, 3, 0])
    hardware.software.speed = 1050
    runGame()

def runGame():
    while hardware.software.lose == False:
        hardware.software.sequence = hardware.software.GenerateSequence()
        hardware.ShowSequence(hardware.software.sequence)
        hardware.GetSequence()
    Start()

Start()
