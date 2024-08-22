from machine import Pin, PWM
from time import sleep

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
        rPin.on()
        piezoPin.duty_u16(500)
        piezoPin.freq(200)
        sleep(1.2)
    elif yButton.value() == True:
        print("Yellow")
        rPin.on()
        gPin.on()
        piezoPin.duty_u16(500)
        piezoPin.freq(300)
        sleep(1.2)
    elif gButton.value() == True:
        print("Green")
        gPin.on()
        piezoPin.duty_u16(500)
        piezoPin.freq(400)
        sleep(1.2)
    elif bButton.value() == True:
        print("Blue")
        bPin.on()
        piezoPin.duty_u16(500)
        piezoPin.freq(500)
        sleep(1.2)
    elif resetButton.value() == True:
        print("Start")
        gPin.on()
        bPin.on()
        rPin.on()
        piezoPin.duty_u16(800)
        piezoPin.freq(600)
        sleep(1.2)
    piezoPin.duty_u16(0)
    gPin.off()
    bPin.off()
    rPin.off()