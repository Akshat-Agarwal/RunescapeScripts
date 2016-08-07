import ctypes
import time
import random

xBankBooth = 514
yBankBooth = 158

xCloseBankBooth = 603
yCloseBankBooth = 51

xDepositInventory = 561
yDepositInventory = 522

xHerb =  211
yHerb = 121

horizontalOffset = 45 #Value needed to get to next column
x = 813 + random.randint(0,3) #813-laptop 1958-Extended screen
print "RandomNum for X %d" % (x-831)  #For logging purpose
y = 435
timeDelay = 0.2
timeMousePressDelay = 0.1 #this is the delay between mouse press up and down to portray real human clicks

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

def cleanColumn(x,y):
	for iterator in range(0, 7):
		time.sleep(0.3)
		ctypes.windll.user32.SetCursorPos(x + random.randint(0,5), y + random.randint(0,8))
		leftClick()
		y = y+38

def cleanHerbsInInventory(x,y):
	for iterator in range(0,4):
		cleanColumn(x,y)
		#move to next column
		x = x + horizontalOffset
		y = 433

for iterator in range(0, 160):
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

	#Withdraw Herbs
	ctypes.windll.user32.SetCursorPos(xHerb, yHerb)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xHerb, yHerb+100)
	leftClick()
	time.sleep(timeDelay)

	#Close bank
	ctypes.windll.user32.SetCursorPos(xCloseBankBooth+random.randint(0,5), yCloseBankBooth+random.randint(0,5))
	leftClick()
	time.sleep(timeDelay)

	cleanHerbsInInventory(x,y)