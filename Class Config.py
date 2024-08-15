from machine import Pin
from time import sleep_ms


#Variable setup
sequence = []
sound = []
playerSeq = []
level = 1
note = 0
speed = 1000

gSound = 261
rSound = 293
ySound = 329
bSound = 349

badSound = 233

gPin = #type:ignore
rPin = #type:ignore
yPin = #type:ignore
bPin = #type:ignore
piezoPin = #type:ignore


class Gameplay:
    pass

class Hardware(Gameplay):

    def __init__(self, softwareClass):
        self.gPin = gPin
        self.rPin = rPin
        self.yPin = yPin
        self.bPin = bPin
        self.piezoPin = piezoPin
        self.softwareClass = softwareClass
    
    def ShowSequence(self):
        pass
    
    def GetSequence(self):
        pass

    def RightSeqence(self):
        pass

    def WrongSequence(self):
        pass


class Software(Gameplay):

    def __init__(self, hardwareClass):
        self.sequence = sequence
        self.sound = sound
        self.playerSeq = playerSeq
        self.level = level
        self.note = note
        self.speed = speed
        self.hardwareClass = hardwareClass
    
    def GenerateSequence(self):
        pass

    def CheckSequence(self):
        pass

