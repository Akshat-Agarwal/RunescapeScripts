import ctypes
import time
import random

xFirstUncut = 1998 
yFirstUncut = 438

xBankBooth = 1727
yBankBooth = 274

xUncutBank = 1420
yUncutBank = 163

xChiselBank = 1471
yChiselBank = 161

xCloseBankBooth = 1818
yCloseBankBooth = 71

xDepositInventory = 1778
yDepositInventory = 517

timeDelay = 0.2
timeMousePressDelay = 0.1 #this is the delay between mouse press up and down to portray real human clicks
timeForGemsToCut = 33

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

def cutGemsInInventory():
	#click chisel
	ctypes.windll.user32.SetCursorPos(1958 + random.randint(0,3), 437)
	time.sleep(0.2)
	leftClick()

	#click gem
	ctypes.windll.user32.SetCursorPos(1998 + random.randint(0,3), 437)
	time.sleep(0.2)
	leftClick()
	time.sleep(0.5)

	#go to gem cutting image and click cut all
	ctypes.windll.user32.SetCursorPos(1557 + random.randint(0,5), 615 + random.randint(0,5))
	time.sleep(0.2)
	rightClick()

	ctypes.windll.user32.SetCursorPos(1539 + random.randint(0,5), 685 + random.randint(0,5))
	time.sleep(0.2)
	leftClick()



for iterator in range(0, 100):
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

	#Take chisel
	ctypes.windll.user32.SetCursorPos(xChiselBank, yChiselBank)
	time.sleep(timeDelay)
	leftClick()
	time.sleep(0.2)

	#Take gems
	ctypes.windll.user32.SetCursorPos(xUncutBank, yUncutBank)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xUncutBank, yUncutBank+100)
	leftClick()
	time.sleep(timeDelay)

	#Close bank
	ctypes.windll.user32.SetCursorPos(xCloseBankBooth+random.randint(0,5), yCloseBankBooth+random.randint(0,5))
	time.sleep(timeDelay)
	leftClick()
	time.sleep(timeDelay)

	cutGemsInInventory()

	#Wait for gems to cut
	time.sleep(timeForGemsToCut)