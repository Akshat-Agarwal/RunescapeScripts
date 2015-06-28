import ctypes
import time
import random

xBankBooth = 1727
yBankBooth = 274

xCloseBankBooth = 1818
yCloseBankBooth = 85

xDepositInventory = 1778
yDepositInventory = 517

xIron = 1759
yIron = 416

xCoal = 1465
yCoal = 273

xSmelterMap = 1900
ySmelterMap = 564
xSmelterMap2 = 1515
ySmelterMap2 = 658

xToBank1 = 2060
yToBank1 = 313
xToBank2 = 1893
yToBank2 = 321


xFurnace = 1562
yFurnace = 573

xSteelBar = 1557 
ySteelBar = 615

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
#TEST
#TEST END
for iterator in range(1, 2):
	# Standing at smelter room, go to bank
	ctypes.windll.user32.SetCursorPos(xBankBooth, yBankBooth)
	time.sleep(timeDelay+0.5)
	print "Log1: xBank: %d yBank: %d" % (xBankBooth,yBankBooth)
	leftClick()
	time.sleep(1)

	ctypes.windll.user32.SetCursorPos(xDepositInventory, yDepositInventory)
	time.sleep(timeDelay)
	leftClick()
	time.sleep(1)

	#Bank is open, right click on iron and get 9
	ctypes.windll.user32.SetCursorPos(xIron, yIron)
	leftClick()
	time.sleep(timeDelay)

	#get 9*2 coal
	ctypes.windll.user32.SetCursorPos(xCoal, yCoal)
	rightClick()
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(xCoal, yCoal+100)
	leftClick()
	time.sleep(timeDelay)

	#Close bank
	ctypes.windll.user32.SetCursorPos(xCloseBankBooth+random.randint(0,5), yCloseBankBooth+random.randint(0,5))
	leftClick()
	time.sleep(timeDelay)

	print "Log2: Got items from bank"

	# #Walk to Smelter in 4 steps
	# for iterator in range(1, 4):
	# 	ctypes.windll.user32.SetCursorPos(xSmelterMap, ySmelterMap)
	# 	leftClick()
	# 	time.sleep(4)

	# time.sleep(4)
	# ctypes.windll.user32.SetCursorPos(xSmelterMap2, ySmelterMap2)
	# leftClick()
	# # #Character is in the smelter room, click on furnace
	# ctypes.windll.user32.SetCursorPos(xFurnace, yFurnace)
	# time.sleep(timeDelay+0.5)
	# leftClick()
	# # time.sleep(timeDelay)
	# # time.sleep(10)

	# # Click on steel bar
	# ctypes.windll.user32.SetCursorPos(xSteelBar, ySteelBar)
	# time.sleep(timeDelay+0.5)
	# rightClick()
	# time.sleep(timeDelay)

	# ctypes.windll.user32.SetCursorPos(xSteelBar, ySteelBar+56)
	# leftClick()
	# time.sleep(timeDelay)

	# #wait to smelt all bars
	# time.sleep(30)

	# #Walk back to the bank
	# ctypes.windll.user32.SetCursorPos(xToBank1, yToBank1)
	# time.sleep(timeDelay)
	# leftClick()
	# time.sleep(7)

	# ctypes.windll.user32.SetCursorPos(xToBank2, yToBank2)
	# time.sleep(timeDelay)
	# leftClick()
	# time.sleep(5)



