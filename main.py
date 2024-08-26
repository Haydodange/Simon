
from ClassConfig import *


software = Software()
hardware = Hardware()

sequence = []
playerSeq = []
level = 1
note = 0
speed = 1050

sequence = software.GenerateSequence()
hardware.ShowSequence(sequence)
hardware.GetSequence()


