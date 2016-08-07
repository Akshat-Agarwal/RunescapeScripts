import ctypes
import time
import random

xFirstUncut = 1998 
yFirstUncut = 438

xBankBooth = 514
yBankBooth = 158

xUncutBank = 255
yUncutBank = 126

xChiselBank = 206
yChiselBank = 123

xCloseBankBooth = 603
yCloseBankBooth = 51

xDepositInventory = 561
yDepositInventory = 522

timeDelay = 0.2
timeMousePressDelay = 0.1 #this is the delay between mouse press up and down to portray real human clicks
timeForGemsToCut = 10

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
def rightClick():
	ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0,0) # right down
	time.sleep(timeMousePressDelay)
	ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0,0) # right up
	return 

def leftClick():
	ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # left down
	time.sleep(timeMousePressDelay)
	ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # left up
	return 

def makePotionsInInventory():
	#click Vial
	ctypes.windll.user32.SetCursorPos(863 + random.randint(0,3), 555)
	time.sleep(0.2)
	leftClick()

	#click Herb
	ctypes.windll.user32.SetCursorPos(903 + random.randint(0,3), 548)
	time.sleep(0.2)
	leftClick()
	time.sleep(0.6)

	#go to herb mixing image and click make all
	ctypes.windll.user32.SetCursorPos(259 + random.randint(0,5), 607 + random.randint(0,5))
	time.sleep(0.3)
	rightClick()

	ctypes.windll.user32.SetCursorPos(240 + random.randint(0,5), 679 + random.randint(0,5))
	time.sleep(0.2)
	leftClick()



for iterator in range(0, 268):
	#open bank 
	ctypes.windll.user32.SetCursorPos(xBankBooth, yBankBooth)
	time.sleep(timeDelay+0.5)
	print "Log1: xBank: %d yBank: %d" % (xBankBooth,yBankBooth)
	leftClick()
	time.sleep(1)

	#Deposit everything
	ctypes.windll.user32.SetCursorPos(xDepositInventory, yDepositInventory)
	time.sleep(timeDelay)
	leftClick()
	time.sleep(0.2)

	#Take vials
	ctypes.windll.user32.SetCursorPos(xChiselBank, yChiselBank)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xChiselBank, yChiselBank+65)
	leftClick()
	time.sleep(0.2)

	#Take gems
	ctypes.windll.user32.SetCursorPos(xUncutBank, yUncutBank)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xUncutBank, yUncutBank+65)
	leftClick()
	time.sleep(timeDelay)

	#Close bank
	ctypes.windll.user32.SetCursorPos(xCloseBankBooth+random.randint(0,5), yCloseBankBooth+random.randint(0,5))
	time.sleep(timeDelay)
	leftClick()
	time.sleep(timeDelay)

	makePotionsInInventory()

	#Wait for gems to cut
	time.sleep(timeForGemsToCut)