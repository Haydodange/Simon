from machine import Pin
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

gPin = Pin(12, Pin.OUT)
rPin = Pin(11, Pin.OUT)
bPin = Pin(13, Pin.OUT)
piezoPin = Pin(16, Pin.OUT)


class Game:
    pass
    
class Hardware(Game):

    def __init__(self):
        self.gPin = gPin
        self.rPin = rPin
        self.bPin = bPin
        self.piezoPin = piezoPin
    
    def ShowSequence(self, displaySequence):
        self.displaySequence = displaySequence

        for x in displaySequence:
            print(x)




    def GetSequence(self):
        pass

    def RightSeqence(self):
        pass

    def WrongSequence(self):
        pass


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

    def CheckSequence(self):
        if playerSeq == sequence:
            Hardware.RightSeqence
        else:
            Hardware.WrongSequence

