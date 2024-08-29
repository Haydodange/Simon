from machine import Pin, PWM
from time import sleep_ms
from random import randint
from gpio_lcd import GpioLcd

#Variable setup
sequence = []
playerSeq = []
level = 1
note = 0
speed = 1020
lose = 0

gSound = 200
rSound = 300
ySound = 400
bSound = 500

badSound = 233

gPin = Pin(13, Pin.OUT)
rPin = Pin(14, Pin.OUT)
bPin = Pin(12, Pin.OUT)
piezoPin = PWM(Pin(22))

rButton = Pin(17, Pin.IN)
yButton = Pin(18, Pin.IN)
gButton = Pin(19, Pin.IN)
bButton = Pin(20, Pin.IN)
resetButton = Pin(16, Pin.IN)

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

class Game:
    pass
    
class Hardware(Game):

    def __init__(self):
        self.gPin = gPin
        self.rPin = rPin
        self.bPin = bPin
        self.piezoPin = piezoPin
        self.software = Software()
    
    def ShowSequence(self):
        for x in self.software.sequence:
            if x == 0:
                rPin.on()
                piezoPin.freq(300)
                piezoPin.duty_u16(1000)
            elif x == 1:
                gPin.on()
                piezoPin.freq(gSound)
                piezoPin.duty_u16(1000)
            elif x == 2:
                bPin.on()
                piezoPin.freq(bSound)
                piezoPin.duty_u16(1000)
            elif x == 3:
                rPin.on()
                gPin.on()
                piezoPin.freq(ySound)
                piezoPin.duty_u16(1000)
            sleep_ms(self.software.speed)
            print(self.software.speed)
            rPin.off()
            gPin.off()
            bPin.off()
            piezoPin.duty_u16(0)
            sleep_ms(int(self.software.speed/10))
            
    def GetSequence(self):
        #global playerSeq

        for i in range(len(self.software.sequence)):
            while rButton.value() == False and yButton.value() == False and gButton.value() == False and bButton.value() == False:
                sleep_ms(50)       
            else:
                if rButton.value() == True:
                    self.software.playerSeq.append(0)
                    rPin.on()
                    piezoPin.freq(rSound)
                    piezoPin.duty_u16(1000)
                elif yButton.value() == True:
                    self.software.playerSeq.append(3)
                    rPin.on()
                    gPin.on()
                    piezoPin.freq(ySound)
                    piezoPin.duty_u16(1000)
                elif gButton.value() == True:
                    self.software.playerSeq.append(1)
                    gPin.on()
                    piezoPin.freq(gSound)
                    piezoPin.duty_u16(1000)
                elif bButton.value() == True:
                    self.software.playerSeq.append(2)
                    bPin.on()
                    piezoPin.freq(bSound)
                    piezoPin.duty_u16(1000)
                sleep_ms(self.software.speed)
                rPin.off()
                gPin.off()
                bPin.off()
                piezoPin.duty_u16(0)
            if self.software.playerSeq[i] != self.software.sequence[i]:
                print(f"Player {self.software.playerSeq}")
                print(f"Sequence {self.software.sequence}")
                print(self.software.sequence)
                self.software.WrongSequence()
        if self.software.playerSeq == self.software.sequence:
            print(f"Player {self.software.playerSeq}")
            print(f"Sequence {self.software.sequence}")
            self.software.RightSeqence()
        else:
            print(f"Player {self.software.playerSeq}")
            print(f"Sequence {self.software.sequence}")
            print(self.software.sequence)
            self.software.WrongSequence()

class Software(Game):

    def __init__(self):
        self.sequence = sequence
        self.playerSeq = playerSeq
        self.level = level
        self.note = note
        self.speed = speed
    
    def GenerateSequence(self):
        lcd.putstr("Simon Level " + str(self.level)) 
        sleep_ms(2000)
        lcd.clear()
        self.sequence.append(randint(0,3))
        self.speed -= 50
        self.level += 1
        return self.sequence
            
    def RightSeqence(self):
        self.playerSeq = []

    def WrongSequence(self):
        #global sequence, playerSeq, level, note, speed, lose
        self.sequence = []
        self.playerSeq = []
        self.level = 1
        self.note = 0
        self.speed = 1020
        lcd.putstr('You lost')
        sleep_ms(2000)
        lcd.clear()
        lcd.putstr('Press Start To  Play Again')
        sleep_ms(2000)
        lcd.clear()
        while resetButton.value() == False:
            sleep_ms(50)
        Software.GenerateSequence(self)
  


