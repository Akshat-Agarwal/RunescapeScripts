import ctypes
import time
import random

xEnchantSpell = 1997 #Emerald = 1997, Sapphire = 2071
yEnchantSpell = 490 #Emerald = 490, Sapphire = 443

xBankBooth = 1727
yBankBooth = 274

xSapphireRing = 1420
ySapphireRing = 163

xRecoilRing = 1996
yRecoilRing = 436

xCloseBankBooth = 1818
yCloseBankBooth = 71

initialYValue = 469
horizontalOffset = 40 #Value needed to get to next column
x = 1958 + random.randint(0,3) #831-laptop 1958-Extended screen
print "RandomNum for X %d" % (x-831)  #For logging purpose
y = initialYValue
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

def EnchantSmallColumnItems(x,y):
	for iterator in range(0, 6): #Change this range to 0,5 if having noted items on bottom left of inventory
		time.sleep(1.5)
		ctypes.windll.user32.SetCursorPos(xEnchantSpell, yEnchantSpell)
		time.sleep(0.1)
		leftClick()
		time.sleep(timeDelay)
		print "We're on location %d %d" % (x,y)
		ctypes.windll.user32.SetCursorPos(x + random.randint(0,5), y + random.randint(0,8))
		leftClick()
		y = y+38

def EnchantLargeColumnItems(x,y):
	for iterator in range(0, 7):
		time.sleep(1.5)
		ctypes.windll.user32.SetCursorPos(xEnchantSpell, yEnchantSpell)
		time.sleep(0.1)
		leftClick()
		time.sleep(timeDelay)
		print "We're on location %d %d" % (x,y)
		ctypes.windll.user32.SetCursorPos(x + random.randint(0,5), y + random.randint(0,8))
		leftClick()
		y = y+38

def EnchantInventory(x,y):
	EnchantSmallColumnItems(x,y)

	#move to next column
	x = x + horizontalOffset
	y = 433

	for iterator in range(0, 3):
		EnchantLargeColumnItems(x,y)

		#move to next column
		x = x + horizontalOffset
		y = 433

for iterator in range(0, 150):
	#open bank 
	ctypes.windll.user32.SetCursorPos(xBankBooth, yBankBooth)
	time.sleep(timeDelay+0.5)
	print "Log1: xBank: %d yBank: %d" % (xBankBooth,yBankBooth)
	leftClick()
	time.sleep(1)

	#Deposit recoil rings
	ctypes.windll.user32.SetCursorPos(xRecoilRing, yRecoilRing)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xRecoilRing, yRecoilRing+100)
	leftClick()
	time.sleep(timeDelay)

	#Take Sapphire Rings
	ctypes.windll.user32.SetCursorPos(xSapphireRing, ySapphireRing)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xSapphireRing, ySapphireRing+100)
	leftClick()
	time.sleep(timeDelay)

	#Close bank
	ctypes.windll.user32.SetCursorPos(xCloseBankBooth+random.randint(0,5), yCloseBankBooth+random.randint(0,5))
	leftClick()
	time.sleep(timeDelay)

	EnchantInventory(x,y)
