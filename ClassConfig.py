from machine import Pin, PWM
from time import sleep_ms
from random import randint


#Variable setup
sequence = []
playerSeq = []
level = 1
note = 0
speed = 1050

gSound = 200
rSound = 300
ySound = 400
bSound = 500

badSound = 233

gPin = Pin(13, Pin.OUT)
rPin = Pin(14, Pin.OUT)
bPin = Pin(12, Pin.OUT)
piezoPin = PWM(Pin(26))

rButton = Pin(17, Pin.IN)
yButton = Pin(18, Pin.IN)
gButton = Pin(19, Pin.IN)
bButton = Pin(20, Pin.IN)
resetButton = Pin(16, Pin.IN)


class Game:
    pass
    
class Hardware(Game):

    def __init__(self):
        self.gPin = gPin
        self.rPin = rPin
        self.bPin = bPin
        self.piezoPin = piezoPin
    
    def ShowSequence(self):

        for x in sequence:
            if x == 0:
                rPin.on()
                piezoPin.freq(rSound)
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
            sleep_ms(speed)
            rPin.off()
            gPin.off()
            bPin.off()
            piezoPin.duty_u16(0)
            
    def GetSequence(self):
        global playerSeq
        
        for i in range(len(sequence)):
            if rButton.value() == True:
                playerSeq.append(0)
            elif yButton.value() == True:
                playerSeq.append(3)
            elif gButton.value() == True:
                playerSeq.append(1)
            elif bButton.value() == True:
                playerSeq.append(2)       
        

class Software(Game):

    def __init__(self):
        self.sequence = sequence
        self.playerSeq = playerSeq
        self.level = level
        self.note = note
        self.speed = speed
    
    def GenerateSequence(self):
        global sequence, speed
        sequence.append(randint(0,3))
        speed =- 50
        
    
    def RightSeqence(self):
        if playerSeq

    def WrongSequence(self):
        pass

    def CheckSequence(self):
        if playerSeq == sequence:
            Software.RightSeqence
        else:
            Software.WrongSequence


