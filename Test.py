from machine import Pin, PWM
from time import sleep
from gpio_lcd import GpioLcd

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


gSound = 200
rSound = 300
ySound = 400
bSound = 500

gPin = Pin(13, Pin.OUT)
rPin = Pin(14, Pin.OUT)
bPin = Pin(12, Pin.OUT)
piezoPin = PWM(Pin(22))

rButton = Pin(17, Pin.IN)
yButton = Pin(18, Pin.IN)
gButton = Pin(19, Pin.IN)
bButton = Pin(20, Pin.IN)
resetButton = Pin(16, Pin.IN)

while True:
    if rButton.value() == True:
        print("Red")
        lcd.putstr("Red")
        rPin.on()
        piezoPin.duty_u16(200)
        piezoPin.freq(200)
        sleep(1.2)
    elif yButton.value() == True:
        print("Yellow")
        lcd.putstr("Yellow")
        rPin.on()
        gPin.on()
        piezoPin.duty_u16(200)
        piezoPin.freq(300)
        sleep(1.2)
    elif gButton.value() == True:
        print("Green")
        lcd.putstr("Green")
        gPin.on()
        piezoPin.duty_u16(200)
        piezoPin.freq(400)
        sleep(1.2)
    elif bButton.value() == True:
        print("Blue")
        lcd.putstr("Blue")
        bPin.on()
        piezoPin.duty_u16(200)
        piezoPin.freq(500)
        sleep(1.2)
    elif resetButton.value() == True:
        print("Start")
        lcd.putstr("Start")
        gPin.on()
        bPin.on()
        rPin.on()
        piezoPin.duty_u16(200)
        piezoPin.freq(600)
        sleep(1.2)
    piezoPin.duty_u16(0)
    gPin.off()
    bPin.off()
    rPin.off()
    lcd.clear()