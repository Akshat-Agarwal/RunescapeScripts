import ctypes
import time
import random


xOre1 = 1898
yOre1 = 355

xOre2 = 1647
yOre2 = 376

initialYValue = 469
horizontalOffset = 42 #Value needed to get to next column
#x = 1958 + random.randint(0,3) #831-laptop 1958-Extended screen
x = 1958
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

def dropLargeColumnItems(x,y):
	for iterator in range(0, 6):
		print "We're on location %d %d" % (x,y)
		time.sleep(timeDelay)
		ctypes.windll.user32.SetCursorPos(x, y)
		rightClick()

		y = y+38
		time.sleep(timeDelay)

		ctypes.windll.user32.SetCursorPos(x, y)
		leftClick()

def dropLastColumnItems():
	time.sleep(timeDelay)
	rightClick()
	y = initialYValue + (38*5) + 12 #bad hack, need to make methods update value of Y, but currently they are passed by value
	time.sleep(timeDelay)
	ctypes.windll.user32.SetCursorPos(x, y)
	leftClick()

for iterator in range(0, 100):
	for iterator in range(0, 14):
		#Mine from first rock
		ctypes.windll.user32.SetCursorPos(xOre1, yOre1)
		time.sleep(0.2)
		leftClick()
		time.sleep(5)

		#Mine from second rock
		ctypes.windll.user32.SetCursorPos(xOre2, yOre2)
		time.sleep(0.2)
		leftClick()
		time.sleep(5)

	#Drop items
	time.sleep(timeDelay)
	dropLargeColumnItems(x,y)

	#last item
	dropLastColumnItems()

	# move to next column
	x = x + horizontalOffset
	y = 469

	dropLargeColumnItems(x,y)

	#last item
	dropLastColumnItems()

	#move to next column
	x = x + horizontalOffset
	y = 442

	dropLargeColumnItems(x,y)

	#last item
	dropLastColumnItems()

	#move to next column
	x = x + horizontalOffset
	y = 442

	dropLargeColumnItems(x,y)

	#last item
	dropLastColumnItems()

