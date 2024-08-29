from ClassConfig import *
from gpio_lcd import GpioLcd
from time import sleep_ms

hardware = Hardware()

print("Generate sequence")
hardware.software.GenerateSequence()
print(hardware.software.sequence)

print("Right Sequence just clears the player seq")
hardware.software.playerSeq = [0, 2, 3, 1, 3]
print(hardware.software.playerSeq)
hardware.software.RightSeqence()
print(hardware.software.playerSeq)
sleep_ms(1000)

print("""Wrong sequence clears all the variables in the main object""")
hardware.software.sequence = [1, 2 , 3]
hardware.software.playerSeq = [1, 2, 0]
hardware.software.level = 5
hardware.software.note = 72
hardware.software.speed = 15550
print(f"""{hardware.software.sequence}
{hardware.software.playerSeq}
{hardware.software.level}
{hardware.software.note}
{hardware.software.speed}""")
hardware.software.WrongSequence()
print("As well as plays the 'play again' on the LCD")
print(f"""{hardware.software.sequence}
{hardware.software.playerSeq}
{hardware.software.level}
{hardware.software.note}
{hardware.software.speed}""")

hardware.software.speed = 500
print("LED ShowSequence test")
hardware.ShowSequence([0 ,3 ,1 ,2])
sleep_ms(1500)
hardware.ShowSequence([2, 1, 3, 0])

print("Hardware GetSequence test, press the buttons left to right")
hardware.software.sequence = [0, 3, 1, 2]
hardware.GetSequence()

print("Generate sequence")
hardware.software.GenerateSequence()
print(hardware.software.sequence)

hardware.GetSequence()
