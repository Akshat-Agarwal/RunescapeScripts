import ctypes
import time
import random
from random import shuffle

xBankBooth = 514
yBankBooth = 158

xCloseBankBooth = 603
yCloseBankBooth = 51

xDepositInventory = 561
yDepositInventory = 522

xHerb = 211
yHerb = 121

startingInventoryCoordinateX = 815
startingInventoryCoordinateY = 435

horizontalOffset = 43 #Value for next item horizontally right(or left)
verticalOffset = 35 #Value for next item vertically below(or above)

timeDelay = 0.2
timeMousePressDelay = 0.1 #this is the delay between mouse press up and down to portray real human clicks
listOfNumbers = []

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

def cleanHerbsInInventory():
	#fill the list (listOfNumbers) with 28 numbers
	x = startingInventoryCoordinateX
	y = startingInventoryCoordinateY

	for i in range(0,7):
		yNew = y + i*verticalOffset
		for j in range(0,4):
			xNew = x + horizontalOffset*j
			pair = (xNew + random.randint(0,20), yNew + random.randint(0,20))
			listOfNumbers.append(pair)

	print listOfNumbers
	shuffle(listOfNumbers)
	print listOfNumbers

	#pop one tuple at a time and click on it
	for i in range(0, len(listOfNumbers)):
		pair = listOfNumbers.pop(0)
		print pair
		ctypes.windll.user32.SetCursorPos(pair[0], pair[1])
		time.sleep(timeDelay)
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

	cleanHerbsInInventory()