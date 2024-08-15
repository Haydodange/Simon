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

class Software:

    def __init__(self):
        self.sequence = sequence
        self.sound = sound
        self.playerSeq = playerSeq
        self.level = level
        self.note = note
        self.speed = speed
    
    def GenerateSequence(self):
        pass

    def CheckSequence(self):
        pass

class Hardware:

    def __init__(self):
        pass