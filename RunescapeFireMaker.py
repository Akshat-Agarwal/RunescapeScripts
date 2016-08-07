import ctypes
import time
import random

XTinderBox = 831 #1956
YTinderBox = 440

horizontalOffset = 42 #Value needed to get to next column

x = 831 + random.randint(0,3) #831-laptop 1958-Extended screen
initialYValue = 469
y = initialYValue
timeDelay = 0.2
timeMousePressDelay = 0.1 #this is the delay between mouse press up and down to portray real human clicks
lightFireDelay = 5 #This is the time taken to finish lighting the fire

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
def leftClick():
	ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # left down
	time.sleep(timeMousePressDelay)
	ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # left up
	return

def selectTinderBox():
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(XTinderBox, YTinderBox)
	leftClick()

def lightSmallColumnLogs(x,y):
	for iterator in range(1, 7):
		selectTinderBox()
		time.sleep(timeDelay)
		ctypes.windll.user32.SetCursorPos(x, y)
		leftClick()
		time.sleep(lightFireDelay)
		y = y + 38

def lightLargeColumnLogs(x,y):
	for iterator in range(1, 8):
		selectTinderBox()
		time.sleep(timeDelay)
		ctypes.windll.user32.SetCursorPos(x, y)
		leftClick()
		time.sleep(lightFireDelay)
		y = y + 38

#Light the first column
lightSmallColumnLogs(x,y)

x = x + horizontalOffset
y = 442

for iterator in range(1, 4):
	lightLargeColumnLogs(x,y)
	x = x + horizontalOffset
